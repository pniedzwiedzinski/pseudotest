from pseudo_test.models import Task, Score, Test
#KIEDYŚ BĘDZIE REST API

def get_all_tasks():
    """returns All tasks from db in a list"""
    task_list = Task.objects.all().values('name')
    return task_list


def get_all_file_ids():
    """returns All file ids from db in a list"""
    id_list = Score.objects.all().values('file_id')
    return id_list


def get_task_tests(task_id):
    """Takse task_id and returns all tests to this task"""
    test_list = Test.objects.filter(task_id=task_id)
    return test_list
