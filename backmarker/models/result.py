from django.db import models

from backmarker.models.constructor import Constructor
from backmarker.models.driver import Driver
from backmarker.models.race import Race
from backmarker.models.status import Status


class Result(models.Model):
    race = models.ForeignKey(Race, models.PROTECT)
    driver = models.ForeignKey(Driver, models.PROTECT)
    constructor = models.ForeignKey(Constructor, models.PROTECT)
    number = models.IntegerField(null=True)
    grid = models.IntegerField()
    position = models.IntegerField(null=True)
    position_text = models.CharField(max_length=255)
    position_order = models.IntegerField()
    points = models.FloatField()
    laps = models.IntegerField()
    time = models.CharField(max_length=255, null=True)
    milliseconds = models.FloatField(null=True)
    fastest_lap = models.IntegerField(null=True)
    rank = models.IntegerField(null=True)
    fastest_lap_time = models.CharField(max_length=255, null=True)
    fastest_lap_speed = models.CharField(max_length=255, null=True)
    status = models.ForeignKey(Status, models.PROTECT)
