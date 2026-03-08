<!-- AUTO-GENERATED — edit .ai/canonical/ instead -->

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





# Tech Stack

- Primary language: Go
- IaC: Terraform
- CI/CD: GitHub Actions
- Editors: Cursor, VS Code, and JetBrains IDEs

These files in `.ai/canonical/` are the **single source of truth** for AI agents across tools. Edit them directly; all other AI instruction files are generated.



# AI Tooling Setup

This section helps you configure Claude, Cursor, and other AI tools with the right permissions and allow lists for this repo.






