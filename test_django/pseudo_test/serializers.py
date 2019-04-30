from rest_framework import serializers
from .models import Task, Score


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'name', 'description')
