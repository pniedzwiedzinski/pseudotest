from django.http import HttpResponse
from django.shortcuts import render
from .models import Task
import boto3   
from test_django.settings import S3_NAME
import random
s3 = boto3.resource('s3')

def send_answer(request):
    if request.method == "POST":
        uploaded_file = request.FILES['file']
        if (uploaded_file.name[-4:] == ".txt" or uploaded_file.name[-4:] == ".pdc"
            ) and uploaded_file.size < 1000000:
            s3.Bucket(S3_NAME).put_object(
            Key='{0}@{1}'.format(request.POST["task"],file_id()), Body=uploaded_file)

    task_list = []
    task_list_1 = Task.objects.all()
    for task in task_list_1:
        task_list.append(task.name)
    context = {'task_list':task_list}
    return render(request, 'pseudo_test/send_answer.html', context)




def file_id():
    for i in range(100):
        can = 1
        file_id = random.randint(10000,99999)
        object_list = []
        for objects in s3.Bucket(S3_NAME).objects.all():
            object_list.append(objects.key[-5:])
        if file_id in object_list:
            continue
        return file_id