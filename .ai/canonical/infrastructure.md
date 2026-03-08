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

