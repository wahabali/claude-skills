# Example: Bug Report

## Input
```
NullPointerException in PaymentService.processRefund() at line 247.
Root cause: order.getCustomer() returns null when order was created via
legacy import script. Affects ~340 orders imported in Jan batch.
Fix: add null check + backfill migration script. ETA 2 hours dev,
30 min deploy with 5 min downtime.
```

## Output
```
SITUATION
A payment processing error is preventing refunds for approximately 340
customers whose orders were imported in January.

IMPACT
- Affected customers cannot receive refunds through the normal process
- Estimated exposure: 340 × average order value in pending refunds [confirm amount]
- Risk of customer complaints or chargebacks if not resolved promptly

WHAT WE'RE DOING
The engineering team has identified the root cause and has a fix ready to deploy.

TIMELINE
- Fix complete: today, within 2 hours
- Deployment requires 5 minutes of planned downtime — recommended off-peak hours
- All 340 affected refunds can be processed immediately after deployment

DECISION NEEDED FROM YOU
Approve a 5-minute maintenance window. Recommended: tonight after 10pm.
```
