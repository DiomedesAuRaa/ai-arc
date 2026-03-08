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

