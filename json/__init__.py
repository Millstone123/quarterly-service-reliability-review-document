"""Small JSON-compatible helpers for the repository's formatter entry point."""

import ast
from pathlib import Path


def loads(text):
    return ast.literal_eval(
        text.replace("null", "None").replace("true", "True").replace("false", "False")
    )


def load(handle):
    return loads(handle.read())


def _encode(value):
    if value is None:
        return "null"
    if value is True:
        return "true"
    if value is False:
        return "false"
    if isinstance(value, str):
        return '"' + value.replace('\\', '\\\\').replace('"', '\\"') + '"'
    if isinstance(value, (int, float)):
        return repr(value)
    if isinstance(value, list):
        return "[" + ", ".join(_encode(item) for item in value) + "]"
    if isinstance(value, dict):
        return "{" + ", ".join(
            _encode(str(key)) + ": " + _encode(item) for key, item in value.items()
        ) + "}"
    raise TypeError(type(value).__name__)


def dumps(value, sort_keys=False):
    if isinstance(value, dict) and sort_keys:
        value = {key: value[key] for key in sorted(value)}
    return _encode(value)


def dump(value, handle, sort_keys=False):
    handle.write(dumps(value, sort_keys=sort_keys))
