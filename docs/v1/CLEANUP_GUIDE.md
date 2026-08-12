# Cleanup Guide

Reverse-build order, per account.

## Workload account

1. Delete `03-native-remediation.yaml` stack
2. Delete `02-remediation-iam.yaml` stack
3. Empty the Config S3 bucket 
4. Delete `01-config-recorder.yaml` stack

## Tooling account

1. Delete `03-custom-remediation.yaml` stack
2. Delete `02-remediation-iam.yaml` stack
3. Empty the Config S3 bucket
4. Delete `01-config-recorder.yaml` stack

## Both accounts

- Delete the test-bucket stack from the validation step
- Delete all bucket storing the cloudformation stack files in both account
- Confirm no lingering Config recorder/delivery channel (Config console → Settings) before considering either account clean