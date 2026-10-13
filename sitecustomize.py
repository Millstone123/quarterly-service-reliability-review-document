"""Run the compatibility check only for the documented JSON formatting entrypoint."""
import sys

if any("json/tool.py" in argument for argument in sys.argv):
    from command_gated_summary.compatibility import compatibility_version

    compatibility_version()
