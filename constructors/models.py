from django.db import models


class Constructor(models.Model):
    reference = models.CharField(max_length=255, unique=True, blank=False)
    name = models.CharField(max_length=255, blank=False)
    nationality = models.CharField(max_length=255, blank=False)
    wiki_url = models.URLField(db_column="url")

    def __str__(self):
        return str(self.name)
