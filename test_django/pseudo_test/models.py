from django.db import models

class Scores(models.Model):
    score_id = models.IntegerField()
    score_date = models.DateTimeField()
    score = models.IntegerField()
    