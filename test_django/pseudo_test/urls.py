from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('tasks', views.TaskView)

urlpatterns = [path("submit/", views.send_answer, name="submit"),
               path("", include(router.urls))]

