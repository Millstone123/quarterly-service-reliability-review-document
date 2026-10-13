"""Build the canonical report from checkout or installed package data."""
from pathlib import Path
from .compatibility import compatibility_version
from .model import load_fields
from .report import render

PACKAGE_ROOT = Path(__file__).resolve().parent
PROJECT_ROOT = PACKAGE_ROOT.parent
DEFAULT_MANIFEST = PACKAGE_ROOT / "data" / "manifest.csv"
if not DEFAULT_MANIFEST.exists():
    DEFAULT_MANIFEST = PROJECT_ROOT / "data" / "manifest.csv"

def build_document(path=None):
    """Materialize the complete report after the compatibility check."""
    compatibility_version()
    return render(load_fields(DEFAULT_MANIFEST if path is None else path))
