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

BUCKET = "pseudotester"


def lambda_handler(event, context):

    logger.info(f"Using pseudo@{pseudo.__version__}")
    logger.info('got event {}'.format(event))

    KEY = event["Records"][0]["s3"]["object"]["key"]


    try:
        exercise, task_id = KEY.split("%40")
        logger.info(f"Exercise: {exercise}, Task_id: {task_id}")
    except ValueError:
        logger.error('Invalid name: {}'.format(KEY))
        raise

    try:
        logger.info("Starting file download")
        response = s3.get_object(Bucket=BUCKET, Key=f"{exercise}@{task_id}")
        pseudocode = response['Body'].read().decode('utf-8')
        logger.info("File dowload finished")
    except ClientError as e:
        if e.response['Error']['Code'] == "404":
            logger.error(f"The object {KEY} does not exist.")
        else:
            logger.error(str(e))
        raise

    logger.info("Running test...")
    results = test(exercise, pseudocode)

    logger.info(results)

    return {
        'statusCode': 200,
        'body': json.dumps(results)
    }
