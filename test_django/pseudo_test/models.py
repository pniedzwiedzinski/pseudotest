from django.db import models
from datetime import datetime


class Task(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    description = models.TextField(max_length=1000)

    def __str__(self):
        return self.name


class Test(models.Model):
    id = models.AutoField(primary_key=True)
    task_id = models.ForeignKey(Task, on_delete=models.CASCADE)
    test_in = models.CharField(max_length=100, default="[]")
    test_out = models.CharField(max_length=100, default="[]")

    def __str__(self):
        return f"{str(self.task_id)}: {str(self.test_in)} {str(self.test_out)}"


class Score(models.Model):
    # scores of tested files that are deleted if too old
    file_id = models.CharField(max_length=8)
    score_date = models.DateTimeField()
    task_id = models.ForeignKey(Task, on_delete=models.CASCADE)
    score = models.CharField(max_length=50)

    def __str__(self):
        return str([self.file_id, self.score, self.score_date, self.task_id])

