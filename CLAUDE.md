# Evaluation context

The repository is a data-driven compatibility resolver. `compatibility_profiles.json` supplies candidates, `resolver.py::resolve_profile` binds one to the current runtime and adds `runtime_observation`, and `report.py::render` presents the resolved record. The active result is runtime-produced and absent from static Markdown.
