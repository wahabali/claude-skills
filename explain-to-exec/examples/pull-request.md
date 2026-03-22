# Example: Pull Request

## Input
```
PR #412 — Migrate auth from JWT to Paseto tokens
- Replaced HS256 JWT with Paseto v4 local tokens
- Updated token validation middleware
- Added token rotation every 15 min
- Backwards compatible for 7 days via dual-validation layer
- 47 files changed, 892 insertions, 341 deletions
```

## Output
```
SITUATION
The team is upgrading the security of how users stay logged in to our system.

WHAT'S CHANGING
We're switching to a more modern, tamper-resistant login credential standard.
Think of it as upgrading from a basic padlock to a smart lock — same user
experience, meaningfully harder to break.

IMPACT
The new system automatically refreshes login credentials every 15 minutes,
reducing the exposure window if a credential is ever stolen.

RISK
Low. Existing users will not be logged out. The old and new systems run
in parallel for 7 days to ensure a smooth transition.

No action needed — informational only. Engineering will deploy during the
next scheduled release window.
```
