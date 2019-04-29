import os
import pymysql


def execute(query, params):
    connection = pymysql.connect(
        host=os.environ["DB_HOST"],
        user=os.environ["DB_USER"],
        passwd=os.environ["DB_PASSWORD"],
        db=os.environ["DB_NAME"],
        cursorclass=pymysql.cursors.DictCursor,
    )

    try:
        with connection.cursor() as cursor:
            cursor.execute(query, params)
            r = cursor.fetchall()
            connection.commit()
    finally:
        connection.close()

    return r
