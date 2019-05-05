from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register("tasks", views.TaskView, base_name="TaskView")

urlpatterns = [
    path("submit/", views.send_answer, name="submit"),
    path("get/<file_id>", views.get_answer, name="get"),
    path("", include(router.urls)),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

