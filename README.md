# automated-security-remediation

Two AWS Config remediation patterns for an S3 public-access violation, built side by side in separate accounts to compare operational overhead.

- **Workload account** — AWS-native path: Config auto-remediation via an SSM Automation document (`AWS-DisableS3BucketPublicReadWrite`). No custom code; retry/backoff handled by Config's own `MaximumAutomaticAttempts` and `RetryAttemptSeconds` parameters.
- **Tooling account** — Custom path: Config emits a compliance-change event, EventBridge routes it to a Lambda function that re-locks the bucket. Retry/error handling would need to be built by hand.

See `docs/v1/DEPLOYMENT_GUIDE.md` for deploy order and the manual trigger step, and `docs/v1/CLEANUP_GUIDE.md` for teardown.

## Structure

```
automated-security-remediation/
├── README.md
├── docs/
│   └── v1/
│       ├── DEPLOYMENT_GUIDE.md
│       └── CLEANUP_GUIDE.md
└── v1/
    └── cloudformation/
        ├── test-bucket.yaml
        ├── workload/
        │   ├── 01-config-recorder.yaml
        │   ├── 02-remediation-iam.yaml
        │   └── 03-native-remediation.yaml
        └── tooling/
            ├── 01-config-recorder.yaml
            ├── 02-remediation-iam.yaml
            ├── 03-custom-remediation.yaml
            └── index.py
```

`index.py` sits alongside the Tooling stack as a readable copy of the remediation logic — the actual deployed source is the inline `ZipFile` block inside `03-custom-remediation.yaml`.