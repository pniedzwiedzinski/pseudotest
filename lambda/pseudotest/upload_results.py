import os
import pymysql


def upload_results(results, job_id):
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
                "UPDATE pseudo_test_score SET score = %s WHERE file_id = %s",
                (pymysql.escape_string(results), pymysql.escape_string(job_id)),
            )
            connection.commit()
    finally:
        connection.close()
