from pseudo_test.models import Task
#KIEDYŚ BĘDZIE REST API

def get_all_tasks():
    """returns All tasks from db in a list"""
    task_list = []
    task_list_1 = Task.objects.all()
    for task in task_list_1:
        task_list.append(task.name)
    return task_list