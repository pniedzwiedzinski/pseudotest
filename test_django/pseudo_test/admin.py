from django.contrib import admin

from .models import Score, Task, Test


class TaskAdmin(admin.ModelAdmin):
    list_display = ("name", "description")


class TestAdmin(admin.ModelAdmin):
    list_display = ("task_id", "test_in", "test_out")
    list_filter = ("task_id",)


admin.site.register(Score)
admin.site.register(Task, TaskAdmin)
admin.site.register(Test, TestAdmin)
