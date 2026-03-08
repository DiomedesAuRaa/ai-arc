#!/usr/bin/env python3
# .ai/scripts/sync-rules.py

import os
import re
from pathlib import Path

CANONICAL_DIR = Path(".ai/canonical")
CLAUDE_OUT = Path(".ai/claude/CLAUDE.md")
CURSOR_OUT = Path(".ai/cursor/.cursorrules")
COPILOT_OUT = Path(".ai/copilot/copilot-instructions.md")
CURSOR_RULES_DIR = Path(".ai/cursor/rules")

# Tags you embed in canonical markdown to control output
# <!-- claude-only --> ... <!-- /claude-only -->
# <!-- copilot-skip --> ... <!-- /copilot-skip -->
# <!-- cursor-only --> ... <!-- /cursor-only -->
# <!-- terraform-rules --> ... <!-- /terraform-rules -->
# <!-- go-rules --> ... <!-- /go-rules -->


def load_canonical() -> str:
    parts = []
    # Deterministic order
    for f in sorted(CANONICAL_DIR.glob("*.md")):
        parts.append(f.read_text())
    return "\n\n".join(parts)


def strip_tags(text: str, tag: str) -> str:
    """Remove tagged blocks for targets that should not see them."""
    return re.sub(
        rf"<!-- {tag} -->.*?<!-- /{tag} -->",
        "",
        text,
        flags=re.DOTALL,
    )


def extract_tagged(text: str, tag: str) -> str:
    """Extract only content inside a tag."""
    matches = re.findall(
        rf"<!-- {tag} -->(.*?)<!-- /{tag} -->",
        text,
        flags=re.DOTALL,
    )
    return "\n".join(matches)


def condense_for_copilot(text: str) -> str:
    """
    Copilot: strip prose, keep only imperatives.
    Heuristic: keep lines starting with -, *, Never, Always, Do, Don't, Prefer, Avoid, or headings.
    """
    lines = []
    for line in text.splitlines():
        stripped = line.strip()
        if re.match(r"^(#|-|\\*|Never|Always|Do |Don't|Prefer|Avoid)", stripped):
            lines.append(line)
    return "\n".join(lines)


def build_cursor_mdc(text: str, glob: str, description: str) -> str:
    return f"""---
description: {description}
globs: {glob}
alwaysApply: false
---

{text}
"""


def sync() -> None:
    canonical = load_canonical()

    # Claude: full fidelity, everything included
    CLAUDE_OUT.parent.mkdir(parents=True, exist_ok=True)
    CLAUDE_OUT.write_text(
        "<!-- AUTO-GENERATED: edit canonical files in .ai/canonical/ -->\n\n"
        + canonical
    )

    # Cursor: strip claude-only blocks, keep rest
    cursor_text = strip_tags(canonical, "claude-only")
    CURSOR_OUT.parent.mkdir(parents=True, exist_ok=True)
    CURSOR_OUT.write_text(
        "# AUTO-GENERATED — edit .ai/canonical/ instead\n\n" + cursor_text
    )

    # Cursor .mdc files: per-language scoping
    CURSOR_RULES_DIR.mkdir(parents=True, exist_ok=True)
    tf_rules = extract_tagged(canonical, "terraform-rules")
    if tf_rules:
        (CURSOR_RULES_DIR / "terraform.mdc").write_text(
            build_cursor_mdc(tf_rules, "**/*.tf,**/*.tfvars", "Terraform rules")
        )
    go_rules = extract_tagged(canonical, "go-rules")
    if go_rules:
        (CURSOR_RULES_DIR / "go.mdc").write_text(
            build_cursor_mdc(go_rules, "**/*.go", "Go rules")
        )

    # Copilot: condensed imperatives only
    copilot_text = strip_tags(canonical, "claude-only")
    copilot_text = strip_tags(copilot_text, "cursor-only")
    copilot_text = strip_tags(copilot_text, "copilot-skip")
    copilot_text = condense_for_copilot(copilot_text)
    COPILOT_OUT.parent.mkdir(parents=True, exist_ok=True)
    COPILOT_OUT.write_text(
        "<!-- AUTO-GENERATED — edit .ai/canonical/ instead -->\n\n" + copilot_text
    )

    print("✅ AI rules synced.")
    print(f"   Claude:  {len(CLAUDE_OUT.read_text())} chars")
    print(f"   Cursor:  {len(CURSOR_OUT.read_text())} chars")
    print(f"   Copilot: {len(COPILOT_OUT.read_text())} chars")


if __name__ == "__main__":
    sync()

