from django.db import models


class Task(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField()
    description = models.TextField()

    def __str__(self):
        return str([self.id, self.name, self.description])



class Test(models.Model):
    id = models.IntegerField(primary_key=True)
    test_in = models.TextField(default="[]")
    test_out = models.TextField(default="[]")
    task_id = models.ForeignKey(Task, on_delete=models.CASCADE)

    def __str__(self):
        return str([self.id, self.name, self.task_id])


class Score(models.Model):
    #scores of tested files that are deleted if too old
    file_id = models.TextField()
    score_date = models.DateTimeField()
    task_id = models.ForeignKey(Task, on_delete=models.CASCADE)
    score = models.IntegerField()

    def __str__(self):
        return str([self.file_id, self.score, self.score_date, self.task_id])

    