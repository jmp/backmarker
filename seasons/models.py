from django.db import models


class Season(models.Model):
    year = models.IntegerField(primary_key=True)
    wiki_url = models.URLField(db_column="url", unique=True)

    def __str__(self):
        return str(self.year)
