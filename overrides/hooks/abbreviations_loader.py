"""
MkDocs hook: load abbreviation tooltips from separate YAML content files.

Loading order (later wins on key collision):
    1. overrides/abbreviations.yml — general definitions shared by every guide.
    2. <guide_dir>/abbreviations.yml — guide-local overrides next to the
       guide's mkdocs.yml. Same key replaces the general definition; new
       keys add to it.

The merged dict is injected into python-markdown's abbr extension via its
`glossary` configuration option (Python-Markdown >= 3.7).

Usage in a guide's mkdocs.yml:

    hooks:
        - ../../overrides/hooks/abbreviations_loader.py
"""

import logging
import os

import yaml

log = logging.getLogger("mkdocs.plugins.abbreviations_loader")

ROOT_ABBR = os.path.normpath(
    os.path.join(os.path.dirname(__file__), "..", "abbreviations.yml")
)


def _load(path):
    if not os.path.exists(path):
        return {}
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f) or {}


def on_config(config, **kwargs):
    base = _load(ROOT_ABBR)

    guide_dir = os.path.dirname(config["config_file_path"])
    override_path = os.path.join(guide_dir, "abbreviations.yml")
    overrides = _load(override_path)

    glossary = {**base, **overrides}

    if not glossary:
        log.info("no abbreviation entries found; skipping")
        return config

    if "abbr" not in config["markdown_extensions"]:
        config["markdown_extensions"].append("abbr")
    config["mdx_configs"].setdefault("abbr", {})
    config["mdx_configs"]["abbr"]["glossary"] = glossary

    log.info(
        "loaded %d abbreviation entries (%d general + %d guide override)",
        len(glossary),
        len(base),
        len(overrides),
    )
    return config
