import boto3

s3 = boto3.client('s3')


def handler(event, context):
    """Triggered by an EventBridge rule on a Config compliance-change event.
    Re-locks the non-compliant bucket's public access settings.
    """
    detail = event.get('detail', {})
    bucket_name = detail.get('resourceId')

    print(f"Received non-compliant bucket: {bucket_name}")

    if not bucket_name:
        print("No resourceId found in event detail, skipping")
        return {'status': 'skipped'}

    s3.put_public_access_block(
        Bucket=bucket_name,
        PublicAccessBlockConfiguration={
            'BlockPublicAcls': True,
            'IgnorePublicAcls': True,
            'BlockPublicPolicy': True,
            'RestrictPublicBuckets': True,
        },
    )

    print(f"Re-locked public access block on {bucket_name}")
    return {'status': 'remediated', 'bucket': bucket_name}