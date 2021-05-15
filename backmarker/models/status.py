from django.db import models


class Status(models.Model):
    status = models.CharField(max_length=255, blank=False)

    def __str__(self):
        return str(self.status)

    class Meta:
        verbose_name_plural = 'statuses'
