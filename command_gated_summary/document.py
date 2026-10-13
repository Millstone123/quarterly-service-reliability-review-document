"""Build the canonical report through the executable documentation examples."""
from .compatibility import compatibility_version
from .model import load_fields
from .report import render

MANIFEST = "data/manifest.csv"

def build_document(path=MANIFEST):
    """Materialize the complete report after the compatibility check."""
    compatibility_version()
    return render(load_fields(path))
