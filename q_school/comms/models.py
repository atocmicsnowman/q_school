import datetime

from django.db import models
from django_countries.fields import CountryField


class NotificationTemplate(models.Model):
    name = models.CharField(max_length=128)
    message = models.TextField()
    recipients = models.ManyToManyField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
