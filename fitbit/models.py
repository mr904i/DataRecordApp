from django.db import models

class HourSteps(models.Model):
    hour_steps = models.IntegerField()
    time = models.DateTimeField(auto_now_add=True)

