import os
from uuid import uuid4

import boto3
from django.http import HttpResponse, JsonResponse, Http404
from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.response import Response

from test_django.settings import S3_NAME

from .api.dbhandlers import get_all_file_ids, get_all_tasks
from .models import Task, Score
from .serializers import TaskSerializer

import json
from datetime import datetime, timedelta

s3 = boto3.client("s3")


def send_answer(request):
    if request.method == "POST":
        uploaded_file = request.FILES["file"]

        valid_extension = uploaded_file.name[-4:] in {".txt", ".pdc"}
        file_is_less_than_1MB = uploaded_file.size < 1048576

        if valid_extension and file_is_less_than_1MB:

            # Check if task exists
            task = Task.objects.filter(id=request.POST["task"]).first()
            if task is None:
                return JsonResponse({"result": "error", "message": "invalid task"})

            # Upload to S3
            file_id = get_file_id()
            s3.put_object(
                Bucket=S3_NAME,
                Key="{0}@{1}".format(request.POST["task"], file_id),
                Body=uploaded_file.read(),
            )

            # Save to DB
            new_score = Score(
                file_id=file_id, task_id=task, score="", score_date=datetime.now()
            )
            new_score.save()

            return JsonResponse({"result": "success", "message": file_id})
        else:
            return JsonResponse(
                {"result": "error", "message": "wrong file format or size"}
            )

    context = {"task_list": get_all_tasks()}
    return render(request, "pseudo_test/send_answer.html", context)


def get_file_id():
    while True:
        new_file_id = uuid4().hex[:8]
        if Score.objects.filter(file_id=new_file_id):
            continue
        return new_file_id


def get_answer(request, file_id):
    score = Score.objects.filter(file_id=file_id).first()

    if score is None:
        raise Http404('{"result": "error", message: "id does not exist"}')

    # Remove timezone info
    date = score.score_date.replace(tzinfo=None)

    if datetime.now() - date > timedelta(minutes=15):
        return JsonResponse({"status": "error"})
    elif score.score == "":
        return JsonResponse({"status": "pending"})
    return JsonResponse({"status": json.loads(score.score)})


class TaskView(viewsets.ViewSet):
    def list(self, request):
        queryset = Task.objects.all()
        serializer = TaskSerializer(queryset, many=True)
        return Response(serializer.data)
