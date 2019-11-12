from django.db import models

class Log(models.Model):
    date = models.DateField()
    # NB: This will be taken in km
    distance = models.FloatField()
    # NB: In this case I am taking one figure in minutes, but there's a good case for taking hour, minute, and second values
    time = models.IntegerField()
    # NB: This would usually be part of a user profile, but for simplicity it is added here.
    weight = models.FloatField()
