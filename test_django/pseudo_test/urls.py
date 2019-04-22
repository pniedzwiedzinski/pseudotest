from django.urls import path, include
from . import views

urlpatterns = [
    path('submit/', views.send_answer, name='submit'),
]

