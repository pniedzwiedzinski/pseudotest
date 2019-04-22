from django.http import HttpResponse
from django.shortcuts import render
from .models import Task
import boto3   
from test_django.settings import S3_NAME
import os
import hashlib
from .api.dbhandlers import get_all_tasks, get_all_file_ids
s3 = boto3.resource('s3')

def send_answer(request):
    if request.method == "POST":
        uploaded_file = request.FILES['file']
        if (uploaded_file.name[-4:] == ".txt" or uploaded_file.name[-4:] == ".pdc"
            ) and uploaded_file.size < 1000000:
            file_id = get_file_id()
            s3.Bucket(S3_NAME).put_object(
            Key='{0}@{1}'.format(request.POST["task"],file_id), Body=uploaded_file)
            return {'result':'success','message':file_id}
        else:
            return {'result':'error','message':'wrong file format or size'}

    context = {'task_list':get_all_tasks()}
    return render(request, 'pseudo_test/send_answer.html', context)


def get_file_id():
    while True:
        can = 1
        new_file_id = hashlib.md5(os.urandom(32)).hexdigest()[:8]
        if Score.objects.filter(file_id=new_file_id):
            continue
        return new_file_id
