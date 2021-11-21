from django.db import models


class Event(models.Model):
    session_id = models.CharField(blank=False, max_length=250)
    category = models.CharField(blank=False, max_length=100)
    name = models.CharField(blank=False, max_length=100)
    data = models.TextField()
    timestamp = models.DateTimeField(blank=False)
