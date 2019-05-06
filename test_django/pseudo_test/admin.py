from django.contrib import admin

from .models import Score, Task, Test


class TaskAdmin(admin.ModelAdmin):
    list_display = ("name", "description")


admin.site.register(Score)
admin.site.register(Task, TaskAdmin)
admin.site.register(Test)
