from django.db import models


class Circuit(models.Model):
    reference = models.CharField(max_length=255, unique=True, blank=False)
    name = models.CharField(max_length=255, blank=False)
    location = models.CharField(max_length=255, blank=False)
    country = models.CharField(max_length=255, blank=False)
    latitude = models.FloatField()
    longitude = models.FloatField()
    altitude = models.IntegerField()
    wiki_url = models.URLField(db_column="url", unique=True)

    def __str__(self):
        return self.name
