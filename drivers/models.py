from django.db import models


class Driver(models.Model):
    reference = models.CharField(max_length=255, unique=True, blank=False)
    number = models.IntegerField(null=True)
    code = models.CharField(max_length=3, null=True)
    first_name = models.CharField(max_length=255, blank=False)
    last_name = models.CharField(max_length=255, blank=False)
    date_of_birth = models.DateField()
    nationality = models.CharField(max_length=255, blank=False)
    wiki_url = models.URLField(db_column="url", unique=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
