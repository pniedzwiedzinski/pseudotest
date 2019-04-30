from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('tasks', views.TaskView, base_name='TaskView')
router.register('scores', views.ScoreView, base_name='ScoreView')

urlpatterns = [path("submit/", views.send_answer, name="submit"),
               path("get/<xd>", views.get_answer, name="get"),
               path("", include(router.urls))]

