# ai-arc

This repository contains a canonical AI rules system that keeps different tools (Claude, Cursor, Copilot) in sync from a single source of truth.

The canonical files live in `.ai/canonical/`. All other AI instruction files are generated from these documents via `.ai/scripts/sync-rules.py`.

## Layout

- `.ai/canonical/`: Source-of-truth markdown files edited by humans.
- `.ai/scripts/sync-rules.py`: Script that generates tool-specific instruction files.
- `.ai/claude/CLAUDE.md`: Full-fidelity instructions for Claude (auto-generated).
- `.ai/cursor/.cursorrules` and `.ai/cursor/rules/*.mdc`: Cursor rules (auto-generated).
- `.ai/copilot/copilot-instructions.md`: Condensed instructions for GitHub Copilot (auto-generated).
- `.claude/CLAUDE.md`, `.cursorrules`, `.github/copilot-instructions.md`: Symlinks pointing to the generated files above.

## Usage

- Edit only the markdown files in `.ai/canonical/`.
- Run `python3 .ai/scripts/sync-rules.py` locally to regenerate all AI instruction files.
- Do not edit generated files directly; they include headers indicating they are auto-generated.

