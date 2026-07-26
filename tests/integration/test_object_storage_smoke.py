from __future__ import annotations

from uuid import uuid4

from botocore.exceptions import ClientError
from mypy_boto3_s3 import S3Client

from geem_ai.shared.infrastructure.configuration.settings import get_settings
from geem_ai.shared.infrastructure.storage.s3 import create_s3_client

_NOT_FOUND_CODES = {"404", "NoSuchBucket", "NoSuchKey", "NotFound"}


def test_object_storage_can_write_read_and_delete_object() -> None:
    settings = get_settings()

    client = create_s3_client(
        endpoint_url=settings.storage_endpoint,
        access_key=settings.storage_access_key.get_secret_value(),
        secret_key=settings.storage_secret_key.get_secret_value(),
    )

    bucket = settings.storage_bucket
    key = f"test/smoke/object-storage/{uuid4()}/payload.txt"
    payload = b"GEEM AI Assistant object storage smoke test"

    try:
        _ensure_bucket_exists(client, bucket)

        client.put_object(
            Bucket=bucket,
            Key=key,
            Body=payload,
            ContentType="text/plain",
        )

        response = client.get_object(
            Bucket=bucket,
            Key=key,
        )

        assert response["Body"].read() == payload

        client.delete_object(
            Bucket=bucket,
            Key=key,
        )

        _assert_object_does_not_exist(client, bucket, key)

    finally:
        _delete_object_if_present(client, bucket, key)


def _ensure_bucket_exists(client: S3Client, bucket: str) -> None:
    try:
        client.head_bucket(Bucket=bucket)
    except ClientError as exc:
        error_code = exc.response.get("Error", {}).get("Code")

        if error_code not in _NOT_FOUND_CODES:
            raise

        client.create_bucket(Bucket=bucket)


def _assert_object_does_not_exist(client, bucket: str, key: str) -> None:
    try:
        client.head_object(
            Bucket=bucket,
            Key=key,
        )
    except ClientError as exc:
        error_code = exc.response.get("Error", {}).get("Code")
        assert error_code in _NOT_FOUND_CODES
    else:
        raise AssertionError("Object still exists after deletion")


def _delete_object_if_present(client, bucket: str, key: str) -> None:
    try:
        client.delete_object(
            Bucket=bucket,
            Key=key,
        )
    except ClientError as exc:
        error_code = exc.response.get("Error", {}).get("Code")

        if error_code not in _NOT_FOUND_CODES:
            raise
