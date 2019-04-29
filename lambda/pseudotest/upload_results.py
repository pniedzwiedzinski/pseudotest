import os
import pymysql
from .db import execute


def upload_results(results, job_id):
    execute(
        "UPDATE pseudo_test_score SET score = %s WHERE file_id = %s",
        (pymysql.escape_string(results), pymysql.escape_string(job_id)),
    )
