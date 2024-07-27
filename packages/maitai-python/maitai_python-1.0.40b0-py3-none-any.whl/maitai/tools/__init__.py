import inspect
import re
from typing import get_type_hints

from maitai_gen.chat import Function, Tool


def tool(func):
    function_description = _extract_function_description(func.__doc__)
    if not function_description:
        raise ValueError("Missing docstring for tool")

    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)

    sig = inspect.signature(func)
    params = sig.parameters

    properties = {}
    required = []
    type_hints = get_type_hints(func)

    descriptions = _extract_param_descriptions(func.__doc__)
    for param_name, param in params.items():
        if param_name in type_hints:
            param_type = type_hints[param_name].__name__
        elif param.default is not param.empty and param.default is not None:
            param_type = type(param.default).__name__
        else:
            param_type = "string"
        properties[param_name] = {"type": param_type}
        if param_name in descriptions:
            properties[param_name]["description"] = descriptions[param_name]
        if param.default is param.empty:
            required.append(param_name)

    wrapper.__tool__ = Tool(
        type="function",
        function=Function(
            name=func.__name__,
            description=function_description,
            parameters={
                "type": "object",
                "properties": properties,
                "required": required,
            },
        )
    )
    return wrapper


def _extract_function_description(docstring):
    lines = docstring.split("\n")
    description = []
    for line in lines:
        if not line.strip().startswith(":"):
            description.append(line.strip())
        else:
            break
    return " ".join(description).strip()


def _extract_param_descriptions(docstring):
    param_descriptions = {}
    param_pattern = re.compile(r":param (\w+): (.+)")
    matches = param_pattern.findall(docstring)
    for param, description in matches:
        param_descriptions[param] = description.strip()
    return param_descriptions
