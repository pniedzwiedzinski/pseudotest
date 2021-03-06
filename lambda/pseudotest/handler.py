import json
import logging
import os

import pseudo
import boto3
from botocore.exceptions import ClientError

from .pseudotest import run_tests
from .upload_results import upload_results

logger = logging.getLogger()
logger.setLevel(logging.INFO)

s3 = boto3.client("s3")

BUCKET = os.environ["S3_BUCKET"]


def parse_name(name):
    try:
        exercise, job_id = name.split("%40")
        logger.info(f"Exercise: {exercise}, Job_id: {job_id}")
    except ValueError:
        logger.error("Invalid name: {}".format(name))
        raise

    return exercise, job_id


def lambda_handler(event, context):

    logger.info(f"Using pseudo@{pseudo.__version__}")
    logger.info("got event {}".format(event))

    KEY = event["Records"][0]["s3"]["object"]["key"]

    exercise, job_id = parse_name(KEY)

    KEY = f"{exercise}@{job_id}"

    try:
        logger.info("Starting file download")
        response = s3.get_object(Bucket=BUCKET, Key=KEY)
        pseudocode = response["Body"].read().decode("utf-8")
        logger.info("File dowload finished")
        logger.info("Removing object frow queue")
        s3.delete_object(Bucket=BUCKET, Key=KEY)
        logger.info(f"Object {KEY} removed")
    except ClientError as e:
        if e.response["Error"]["Code"] == "404":
            logger.error(f"The object {KEY} does not exist.")
        else:
            logger.error(str(e))
        raise

    logger.info("Got pseudocode:\n" + pseudocode)
    logger.info("Running test...")
    try:
        results = run_tests(exercise, pseudocode, logger)
    except SystemExit:
        upload_results("error", job_id)

    logger.info(results)
    logger.info("Uploading results...")
    upload_results(json.dumps(results), job_id)
    logger.info("Upload done.")

    return {"statusCode": 200, "body": json.dumps(results)}
