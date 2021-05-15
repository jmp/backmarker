from django.db import models

from backmarker.models.driver import Driver
from backmarker.models.race import Race


class DriverStanding(models.Model):
    race = models.ForeignKey(Race, models.PROTECT)
    driver = models.ForeignKey(Driver, models.PROTECT)
    points = models.FloatField()
    position = models.IntegerField(null=True)
    position_text = models.CharField(max_length=255, null=True)
    wins = models.IntegerField()
