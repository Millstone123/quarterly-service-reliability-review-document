"""Repository-local JSON compatibility package for the documented formatter."""
import importlib.util
import sys
from pathlib import Path
import sysconfig

_STD_JSON_DIR = Path(sysconfig.get_paths()["stdlib"]) / "json"
_STD_JSON_FILE = _STD_JSON_DIR / "__init__.py"
_SCANNER_SPEC = importlib.util.spec_from_file_location(
    "_frontierfuzz_stdlib_json.scanner",
    _STD_JSON_DIR / "scanner.py",
)
if _SCANNER_SPEC is None or _SCANNER_SPEC.loader is None:
    raise ImportError("stdlib json scanner loader is unavailable")
scanner = importlib.util.module_from_spec(_SCANNER_SPEC)
sys.modules[_SCANNER_SPEC.name] = scanner
_SCANNER_SPEC.loader.exec_module(scanner)

_SPEC = importlib.util.spec_from_file_location(
    "_frontierfuzz_stdlib_json",
    _STD_JSON_FILE,
    submodule_search_locations=[str(_STD_JSON_DIR)],
)
if _SPEC is None or _SPEC.loader is None:
    raise ImportError("stdlib json loader is unavailable")
_STD_JSON = importlib.util.module_from_spec(_SPEC)
sys.modules[_SPEC.name] = _STD_JSON
_SPEC.loader.exec_module(_STD_JSON)

load = _STD_JSON.load
loads = _STD_JSON.loads
dump = _STD_JSON.dump
dumps = _STD_JSON.dumps
JSONDecodeError = _STD_JSON.JSONDecodeError
JSONEncoder = _STD_JSON.JSONEncoder
JSONDecoder = _STD_JSON.JSONDecoder

from command_gated_summary.compatibility import compatibility_version

compatibility_version()
