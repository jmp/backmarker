from django.db import models

from backmarker.models.constructor import Constructor
from backmarker.models.race import Race


class ConstructorStanding(models.Model):
    race = models.ForeignKey(Race, models.PROTECT)
    constructor = models.ForeignKey(Constructor, models.PROTECT)
    points = models.FloatField()
    position = models.IntegerField(null=True)
    position_text = models.CharField(max_length=255, null=True)
    wins = models.IntegerField()
