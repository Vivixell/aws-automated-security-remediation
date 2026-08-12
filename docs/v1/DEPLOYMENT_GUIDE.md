# Deployment Guide

## Prerequisites

- Two accounts, no AWS Config recorder currently running in either.
- Console access with permissions to deploy CloudFormation, IAM, Config, S3, Lambda, EventBridge

## Workload account (native path) — deploy in order

1. `v1/cloudformation/workload/01-config-recorder.yaml` 
2. `v1/cloudformation/workload/02-remediation-iam.yaml`
3. `v1/cloudformation/workload/03-native-remediation.yaml`

## Tooling account (custom path) — deploy in order

1. `v1/cloudformation/tooling/01-config-recorder.yaml` 
2. `v1/cloudformation/tooling/02-remediation-iam.yaml`
3. `v1/cloudformation/tooling/03-custom-remediation.yaml`

## Validation (console, both accounts)

In each account:

1. Create a test S3 bucket, use the `[v1/cloudformation/test-bucket.yaml]()` cloudformation bucket stack.
2. Under Permissions, uncheck "Block all public access"
3. Attach a public-read bucket policy
4. Wait ~5 minutes for the Config recorder to detect the change
5. Watch the bucket get flagged `NON_COMPLIANT` in the Config console

- **Workload:** watch the Config rule's Remediation tab — status should move through in-progress to successful as SSM Automation runs
- **Tooling:** watch the Lambda function's CloudWatch Logs — you should see the "Received non-compliant bucket" / "Re-locked public access block" log lines
- Trigger the non-compliant for each account one after the other has remediated, to observe the flow.
