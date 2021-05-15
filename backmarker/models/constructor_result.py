from django.db import models

from backmarker.models.constructor import Constructor
from backmarker.models.race import Race


class ConstructorResult(models.Model):
    race = models.ForeignKey(Race, models.PROTECT)
    constructor = models.ForeignKey(Constructor, models.PROTECT)
    points = models.FloatField(null=True)
    status = models.CharField(max_length=255, null=True)
