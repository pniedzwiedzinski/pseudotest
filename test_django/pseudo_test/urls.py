from django.urls import path
from . import views

urlpatterns = [
    path('send_answer/', views.send_answer, name='send_answer'),
]

