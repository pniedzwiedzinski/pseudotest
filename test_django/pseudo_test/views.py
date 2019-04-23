import os
from uuid import uuid4

import boto3
from django.http import HttpResponse
from django.shortcuts import render

from test_django.settings import S3_NAME

from .api.dbhandlers import get_all_file_ids, get_all_tasks
from .models import Task

s3 = boto3.resource("s3")


def send_answer(request):
    if request.method == "POST":
        uploaded_file = request.FILES["file"]
        if (
            uploaded_file.name[-4:] == ".txt" or uploaded_file.name[-4:] == ".pdc"
        ) and uploaded_file.size < 1000000:
            file_id = get_file_id()
            s3.Bucket(S3_NAME).put_object(
                Key="{0}@{1}".format(request.POST["task"], file_id), Body=uploaded_file
            )
            return {"result": "success", "message": file_id}
        else:
            return {"result": "error", "message": "wrong file format or size"}

    context = {"task_list": get_all_tasks()}
    return render(request, "pseudo_test/send_answer.html", context)


def get_file_id():
    while True:
        new_file_id = uuid4().hex[:8]
        if Score.objects.filter(file_id=new_file_id):
            continue
        return new_file_id
