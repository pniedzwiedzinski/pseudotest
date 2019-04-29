import os
import json
import pymysql
from .db import execute


def serialize_tests(test_list):
    tests = []

    for r in test_list:
        r["test_in"] = json.loads(r["test_in"])
        r["test_out"] = json.loads(r["test_out"])
        tests.append(r)

    return tests


def get_test(id):
    results = execute(
        "SELECT * FROM pseudo_test_test WHERE task_id_id = %s",
        pymysql.escape_string(str(id)),
    )

    return serialize_tests(results)
