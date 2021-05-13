from django.db import models


class Circuit(models.Model):
    reference = models.CharField(max_length=255, unique=True, blank=False)
    name = models.CharField(max_length=255, blank=False)
    location = models.CharField(max_length=255, blank=False)
    country = models.CharField(max_length=255, blank=False)
    latitude = models.FloatField()
    longitude = models.FloatField()
    altitude = models.IntegerField()
    url = models.URLField(unique=True)

    def __str__(self):
        return self.name
