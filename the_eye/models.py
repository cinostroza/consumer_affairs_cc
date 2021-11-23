from django.db import models


# The RawEventsData model will store the data raw from the apps
class RawEventsData(models.Model):
    data = models.CharField(max_length=2000, blank=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['timestamp']


# The Events model will store the data after it has been processed.
class Events(models.Model):
    application = models.CharField(max_length=250, blank=False)
    session_id = models.CharField(max_length=400, blank=False)
    category = models.CharField(max_length=250)
    name = models.CharField(max_length=250, blank=False)
    data = models.CharField(max_length=2000, blank=False)
    timestamp = models.DateTimeField(blank=False)

    class Meta:
        ordering = ['timestamp']


class Errors(models.Model):
    raw_event = models.ForeignKey(RawEventsData, on_delete=models.CASCADE)
    error_description = models.CharField(max_length=250)
