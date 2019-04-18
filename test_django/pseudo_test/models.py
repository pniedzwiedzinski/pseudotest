from django.db import models

class Scores(models.Model):
    id = models.IntegerField(primary_key=True)
    score_date = models.DateTimeField()
    score = models.IntegerField()

    def __str__(self):
        return str([self.id, self.score, self.score_date])


class Task(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField()
    description = models.TextField()

    def __str__(self):
        return str([self.id, self.name, self.description])
    