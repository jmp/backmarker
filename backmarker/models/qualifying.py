from django.db import models

from backmarker.models.constructor import Constructor
from backmarker.models.driver import Driver
from backmarker.models.race import Race


class Qualifying(models.Model):
    race = models.ForeignKey(Race, models.PROTECT)
    driver = models.ForeignKey(Driver, models.PROTECT)
    constructor = models.ForeignKey(Constructor, models.PROTECT)
    number = models.IntegerField()
    position = models.IntegerField(null=True)
    q1 = models.CharField(max_length=255, null=True)
    q2 = models.CharField(max_length=255, null=True)
    q3 = models.CharField(max_length=255, null=True)
