<!-- AUTO-GENERATED: edit canonical files in .ai/canonical/ -->

# Code Conventions

- Prefer small, composable modules with clear responsibilities.
- Write explicit error handling; avoid silent failures.
- Keep configuration in code or versioned files, not in ad-hoc notes.
- Prefer declarative infrastructure changes via Terraform over manual edits.

These conventions apply across the repo unless overridden in more specific documents (for example, language-specific files in `.ai/canonical/`).



# Infrastructure Rules

Always use data sources instead of hardcoded ARNs.
Never suggest deleting resources without a migration path.
Assume all services are multi-region unless stated.

<!-- claude-only -->
When the user is modifying a Terraform module, reason about
existing state before suggesting resource creation. Check
for implicit dependencies across modules before recommending
a destroy/recreate cycle.
<!-- /claude-only -->

<!-- terraform-rules -->
- All resources must have a `tags` block with at minimum: env, team, managed-by
- Use `for_each` over `count` for resources that may be selectively removed
- Remote state references must use `terraform_remote_state` data sources
<!-- /terraform-rules -->

<!-- go-rules -->
- Explicit error handling only, no panic in library code
- Context must be first arg on all functions touching IO
- All exported functions require godoc
<!-- /go-rules -->



# Security Rules

- Assume zero trust between services; authenticate and authorize every request.
- Never hardcode secrets; use the appropriate secret manager for the environment.
- Prefer least-privilege IAM policies over broad wildcards.
- Treat all user input as untrusted; validate and sanitize at boundaries.

<!-- claude-only -->
When assisting with security-sensitive changes, reason explicitly about
threat models, data classification, and blast radius of potential failures.
Highlight trade-offs rather than silently weakening controls.
<!-- /claude-only -->



# Tech Stack

- Primary language: Go
- IaC: Terraform
- CI/CD: GitHub Actions
- Editors: Cursor, VS Code, and JetBrains IDEs

These files in `.ai/canonical/` are the **single source of truth** for AI agents across tools. Edit them directly; all other AI instruction files are generated.



# AI Tooling Setup

This section helps you configure Claude, Cursor, and other AI tools with the right permissions and allow lists for this repo.

<!-- copilot-skip -->
## Common checklist

- Allow the agent to **read and write** within this repo, especially `.ai/**` and `.github/**`.
- Allow running **safe local commands** such as:
  - `python3 .ai/scripts/sync-rules.py`
  - `git status`, `git diff`, `git add`, `git commit` within this repo
- Prefer running commands **from the repo root** so relative paths like `.ai/...` resolve correctly.
<!-- /copilot-skip -->

<!-- claude-only -->
## Claude-specific notes

- In any workflow or project configuration, include a note that:
  - Canonical AI rules live in `.ai/canonical/`.
  - The main maintenance command is: `python3 .ai/scripts/sync-rules.py`.
- If the workflow supports **tool allow lists**, add:
  - Shell commands limited to this repo.
  - Git commands for basic status/diff/add/commit.
<!-- /claude-only -->

<!-- cursor-only -->
## Cursor-specific notes

- Ensure the agent is allowed to:
  - Run `python3 .ai/scripts/sync-rules.py` from the repo root.
  - Read and update files under `.ai/**` and `.github/**`.
- When prompted, you can paste this as context for permissions:

  - Allow shell commands: `python3 .ai/scripts/sync-rules.py`, `git status`, `git diff`, `git add`, `git commit`.
  - Allow file access: `.ai/**`, `.github/**`, project root.
<!-- /cursor-only -->

