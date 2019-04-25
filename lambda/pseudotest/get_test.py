import os
import pymysql
import json


def serialize_tests(test_list):
    tests = []

    for r in test_list:
        r["test_in"] = json.loads(r["test_in"])
        r["test_out"] = json.loads(r["test_out"])
        tests.append(r)

    return tests


def get_test(id):
    connection = pymysql.connect(
        host=os.environ["DB_HOST"],
        user=os.environ["DB_USER"],
        passwd=os.environ["DB_PASSWORD"],
        db=os.environ["DB_NAME"],
        cursorclass=pymysql.cursors.DictCursor,
    )

    try:
        with connection.cursor() as cursor:
            cursor.execute(
                "SELECT * FROM pseudo_test_test WHERE task_id_id = %s",
                pymysql.escape_string(str(id)),
            )
            results = cursor.fetchall()
    finally:
        connection.close()

    return serialize_tests(results)
