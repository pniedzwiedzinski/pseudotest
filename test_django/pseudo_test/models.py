from django.db import models


class Test(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField()

    def __str__(self):
        return str([self.id, self.name])


class Task(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField()
    test_id = models.ForeignKey(Test,on_delete=models.CASCADE)
    description = models.TextField()

    def __str__(self):
        return str([self.id, self.name, self.test_id, self.description])


class Score(models.Model):
    #scores of tested pseudocodes that are deleted if too old
    id = models.IntegerField(primary_key=True)
    score_date = models.DateTimeField()
    task_id = models.ForeignKey(Task, on_delete=models.CASCADE)
    score = models.IntegerField()

    def __str__(self):
        return str([self.id, self.score, self.score_date])

    