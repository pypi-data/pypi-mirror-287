# Based on: https://til.simonwillison.net/llms/python-react-pattern

from openai import OpenAI
from typing_extensions import Annotated
from typing import Optional
import os
import subprocess
import tempfile

from jinja2 import Template
from pydantic import BaseModel, Field
import instructor

# import logging
# logging.basicConfig(level=logging.DEBUG)

client = instructor.from_openai(OpenAI())
model_name = os.environ.get("KUBLAH_MODEL_NAME", "gpt-4o")


def kubectl(action: str, args: list[str], prompt=True):
    cli = ["kubectl", action] + args
    if prompt:
        if input(f"are you should about running {cli}?") != "yes":
            return "Aborted"

    return (
        subprocess.Popen(" ".join(cli), shell=True, stdout=subprocess.PIPE)
        .stdout.read()
        .decode()
    )


def kubectl_get(args: list[str]):
    """
    kubectl_get is the action to display one or many resources. It is essentially the `kubectl get` command.

    ## Example

    To get all the pods in the foo namespace:

    ```
    Action:
        kubectl_get: ["-n", "foo", "pods"]
    ```

    To inspect the bar pod in the foo namespace:

    ```
    Action:
        kubectl_get: ["-n", "foo", "pods", "bar", "-o", "yaml"]
    ```

    To inspect deploy in the foo namespace:
    ```
    Action:
        kubectl_get: ["-n", "foo", "deploy"]
    ```
    """
    return kubectl("get", args, prompt=False)


def kubectl_delete(args: list[str]):
    """
    kubectl_delete is the action to delete one or many resources. It is essentially the `kubectl delete` command.

    ## Example

    ```
    Action:
        kubectl_delete: ["-n", "foo", "pods", "bar"]
    ```
    """
    return kubectl("delete", args, prompt=True)


def kubectl_apply(args: list[str]):
    """
    kubectl_apply is the action to apply a configuration to a resource. It is essentially the `kubectl apply` command.

    ```
    Action:
        kubectl_apply:
        - |
            apiVersion: v1
            kind: Pod
            metadata:
                name: busybox
            spec:
                containers:
                - image: busybox
                command:
                    - sleep
                    - "3600"
    ```
    """
    content = args[0].encode()
    with tempfile.NamedTemporaryFile(suffix=".yaml") as f:
        f.write(content)
        f.flush()
        return kubectl("apply", ["-f", f.name], prompt=True)


def kubectl_logs(args: list[str]):
    """
    kubectl_logs is the action to display the logs of a container in a pod. It is essentially the `kubectl logs` command.

    ## Example

    To get the logs of the bar container in the bar pod in the foo namespace:

    ```
    Action:
        kubectl_logs: ["-n", "foo", "pod/bar", "-c", "bar"]
    ```
    """
    # xxx: This is a hack to get the logs of the last 100 lines.
    args.append("--tail=100")
    return kubectl("logs", args, prompt=False)


known_actions = {
    "kubectl_get": kubectl_get,
    # "kubectlcreate": kubectl_create,
    "kubectl_delete": kubectl_delete,
    "kubectl_apply": kubectl_apply,
    "kubectl_logs": kubectl_logs,
}


class ReactAction(BaseModel):
    action: str
    args: list[str]


class React(BaseModel):
    question: Annotated[Optional[str], Field(default=None)]
    thought: Annotated[Optional[str], Field(default=None)]
    action: Annotated[Optional[ReactAction], Field(default=None)]
    observation: Annotated[Optional[str], Field(default=None)]
    answer: Annotated[Optional[str], Field(default=None)]


class ChatBot:
    def __init__(self, system="") -> None:
        self.system = system
        self.messages = []
        if self.system:
            self.messages.append({"role": "system", "content": self.system})

    def __call__(self, message: str):
        self.messages.append({"role": "user", "content": message})
        result = self.execute()
        self.messages.append({"role": "assistant", "content": result.model_dump_json()})

        return result

    def execute(self):
        return client.chat.completions.create(
            model=model_name,
            response_model=React,
            messages=self.messages,
            max_retries=3,
        )


prompt = """
You run in a loop of thought, action, bbservation.
At the end of the loop you output an answer.
Use thought to describe your thoughts about the question you have been asked.
Use action to run one of the actions available to you - then return.
observation will be the result of running those actions.

If you know the answer you can skip the Thought and Action steps, and output the Answer directly.

Your available actions are {{ known_actions.keys() }}.

Notes you output must be in format as follows:

```
question: ...
thought: ...
action: ...
```

Or
```
observation: ...
question: ...
thought: ...
action: ...
```
Or
```
answer: ...
```

Here are all the namespaces:
{{ namespaces }}

Here are the details for the actions available to you:

{% for action, func in known_actions.items() %}
# {{ action }}
{{ func.__doc__ }}
{% endfor %}

## Example session:

You are asked "Exec into a pod in the bar pod in the foo namespace interactively using bash"

This is your first output:

```
question: Exec into a pod in the bar pod in the foo namespace interactively using bash
thought: I need to find the namespace that is like foo
action:
    kubectl_get: ["ns" "-o" "name"]
```

You will be called again with this:

```
observation: |
    namespace/default
    namespace/foo-1
thought: I need to find the pod that is like bar in the foo-1 namespace
action: kubectl_get: ["-n", "foo-1", "pods"]
```

You will be called again with this:

```
observation: |
    NAME     READY   STATUS    RESTARTS   AGE
    aaa      1/1     Running   0          2d
    bar-xxx  1/1     Running   0          2d
```

You then output:
```
answer: >
    kubectl exec -it pods/bar-xxx -n foo-1 -- bash
```
"""


prompt = Template(prompt).render(
    namespaces=kubectl_get(["ns", "-o", "name"]).split("\n"),
    known_actions=known_actions,
)


def query(question, max_turns=5):
    i = 0
    bot = ChatBot(prompt)
    next_prompt = question
    while i < max_turns:
        i += 1
        result = bot(next_prompt)

        if result.answer is not None:
            print(f"--- answer: {result.answer}")
            return

        if result.thought is not None:
            print(f"--- thought: {result.thought}")

        if result.action is not None:
            action = result.action

            action_name = action.action
            args = action.args

            print(f"--- running {action_name} {args}")
            observation = known_actions[action_name](args)

            next_prompt = f"Observation: \n{observation}"


# args = " ".join(os.sys.argv[1:])
# query(args)

def main():
    args = " ".join(os.sys.argv[1:])
    query(args)

if __name__ == "__main__":
    main()
