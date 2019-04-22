import json
import logging
import os

import pseudo
import boto3
from botocore.exceptions import ClientError

from pseudotest import test

logger = logging.getLogger()
logger.setLevel(logging.INFO)

s3 = boto3.client('s3')

BUCKET = "pseudo-tester"


def lambda_handler(event, context):

    logger.info(f"Using pseudo@{pseudo.__version__}")
    logger.info('got event {}'.format(event))

    KEY = event["Records"][0]["s3"]["object"]["key"]

    try:
        exercise, task_id = KEY.split("@")
    except ValueError:
        logger.error('Invalid name: {}'.format(KEY))
        raise

    try:
        s3.Bucket(BUCKET).download_file(KEY, 'test.pdc')
    except ClientError as e:
        if e.response['Error']['Code'] == "404":
            logger.error("The object does not exist.")
        else:
            logger.error(str(e))
        raise

    results = test(exercise)

    return {
        'statusCode': 200,
        'body': json.dumps(results)
    }
