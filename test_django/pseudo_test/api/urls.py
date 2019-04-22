from django.urls import path
from .dbhandlers import get_all_file_ids, get_all_tasks

urlpatterns = [
    path('get_ids/', get_all_file_ids, name='get_ids'),
    path('get_tasks', get_all_tasks, name='get_tasks'),
]
