from django.db import models

class DataRecord(models.Model):
    position = models.IntegerField()
    percent = models.FloatField()
    year = models.IntegerField()
    days = models.IntegerField()

    def __str__(self):
        return f"{self.position} ({self.year})"
