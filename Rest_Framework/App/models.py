from django.db import models

# Create your models here.
class Info(models.Model):
    mission_name = models.CharField(max_length=15)
    manufacturers = models.CharField(max_length=50, default='NaN')
    mission_id = models.CharField(max_length=10, default='NaN')
    count = models.IntegerField( default=0)

    def __str__(self):
        return self.mission_name