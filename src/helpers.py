"""
Main functon upload, download and list all files
"""
import boto3
from loguru import logger

from settings import config


session = boto3.Session(
    aws_access_key_id=config.AWS_ACCESS_KEY_ID,
    aws_secret_access_key=config.AWS_SECRET_ACCESS_KEY,
)

s3 = session.resource("s3")
bucket = s3.Bucket(config.BUCKET)


async def s3_upload(contents: bytes, key: str) -> None:
    """
    S3 upload function
    :param contents: file to upload
    :param key: file name
    :return: None
    """
    logger.info(f"Uploading {key} ot S3")
    bucket.put_object(Key=key, Body=contents)
