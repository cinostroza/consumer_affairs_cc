from django.db import models


class Events(models.Model):
    session_id = models.CharField(blank=False, max_length=250)
    category = models.CharField(blank=False, max_length=100)
    name = models.CharField(blank=False, max_length=100)
    data = models.CharField(blank=False, max_length=1200)
    timestamp = models.DateTimeField(blank=False)
    is_validated = models.BooleanField(blank=False, default=False)
    has_errors = models.BooleanField(blank=True, null=True, default=False)

    class Meta:
        ordering = ['timestamp']
