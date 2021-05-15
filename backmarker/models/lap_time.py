from django.db import models

from backmarker.models.driver import Driver
from backmarker.models.race import Race


class LapTime(models.Model):
    race = models.ForeignKey(Race, models.PROTECT)
    driver = models.ForeignKey(Driver, models.PROTECT)
    lap = models.IntegerField()
    position = models.IntegerField(null=True)
    time = models.CharField(max_length=255, null=True)
    milliseconds = models.IntegerField(null=True)
