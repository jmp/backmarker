from django.db import models

from circuits.models import Circuit


class Race(models.Model):
    year = models.IntegerField()
    round = models.IntegerField()
    circuit = models.ForeignKey(Circuit, models.PROTECT)
    name = models.CharField(max_length=255)
    date = models.DateField()
    time = models.TimeField()
    wiki_url = models.URLField(db_column="url", unique=True)

    def __str__(self):
        return f"{self.name} {self.year}"
