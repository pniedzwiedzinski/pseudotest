import json
import logging
import boto3
import pseudo

logger = logging.getLogger()
logger.setLevel(logging.INFO)

s3 = boto3.client('s3')

BUCKET = "pseudo-tester"


def test(exercise):
    with open("test.pdc") as fp:
        pseudocode = fp.read()

    # TODO: Get tests from RDS
    tests = []

    for t in tests:
        instructions = compile(pseudocode)


def lambda_handler(event, context):
    print(pseudo.__version__)
    logger.info('got event {}'.format(event))

    KEY = event["Records"][0]["s3"]["object"]["key"]

    try:
        exercise, task_id = KEY.split("@")
    except ValueError:
        logger.error('Invalid name: {}'.format(KEY))
        raise

    try:
        s3.Bucket(BUCKET).download_file(KEY, 'test.pdc')
    except botocore.exceptions.ClientError as e:
        if e.response['Error']['Code'] == "404":
            logger.error("The object does not exist.")
        else:
            logger.error(str(e))
        raise

    results = test(exercise)

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
