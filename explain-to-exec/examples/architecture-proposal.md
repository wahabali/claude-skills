# Example: Architecture Proposal

## Input
```
Proposing to migrate from monolith to microservices for the reporting module.
Benefits: independent scaling, faster deploys for that team, tech debt reduction.
Cost: 3 engineers × 6 weeks, new infrastructure (~€800/month additional AWS cost),
learning curve on Kubernetes.
```

## Output
```
SITUATION
Engineering is proposing to split our reporting system into its own
independent service, separate from the main product.

WHY IT'S BEING PROPOSED
- The reporting module slows down the whole system during heavy usage
- Any change to it currently requires redeploying the entire product — slow and risky
- Separating it lets the reporting team move faster without affecting other teams

COST
- Engineering: 3 people for 6 weeks
- Ongoing infrastructure: +€800/month
- One-time: 2–3 weeks of reduced velocity while the team ramps up on new tooling

EXPECTED RETURN
- Reporting updates can be deployed in minutes instead of hours
- Reporting load no longer affects checkout, user accounts, or other features
- Foundation for scaling reporting independently during month-end peaks
- Estimated payback: ~4 months in reduced incident risk and deploy time

DECISION NEEDED FROM YOU
Approve budget and headcount allocation for a 6-week project.
Proposed start date: [to be confirmed].
```
