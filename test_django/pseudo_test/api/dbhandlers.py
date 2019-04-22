from pseudo_test.models import Task, Score
from django.http import HttpResponse
#KIEDYŚ BĘDZIE REST API

def get_all_tasks(request):
    """returns All tasks from db in a list"""
    task_list = Task.objects.all().values('name')
    return HttpResponse(task_list)


def get_all_file_ids(request):
    """returns All file ids from db in a list"""
    id_list = Score.objects.all().values('file_id')
    return HttpResponse(id_list)

    