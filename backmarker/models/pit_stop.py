from django.db import models

from backmarker.models.driver import Driver
from backmarker.models.race import Race


class PitStop(models.Model):
    race = models.ForeignKey(Race, models.PROTECT)
    driver = models.ForeignKey(Driver, models.PROTECT)
    stop = models.IntegerField()
    lap = models.IntegerField()
    time = models.TimeField()
    duration = models.CharField(max_length=255, null=True)
    milliseconds = models.IntegerField(null=True)
