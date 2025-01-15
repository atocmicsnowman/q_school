import datetime

from django.db import models
from django_countries.fields import CountryField

from q_school.geography.models import AreaOfOperation
from q_school.registration.models import Pax


class Event(models.Model):
    start = models.DateTimeField()
    end = models.DateTimeField()
    leadership_team = models.ManyToManyField(
        Pax, related_name='leadership_team'
    )
    support_team = models.ManyToManyField(
        Pax, related_name='support_team'
    )


class Calendar(models.Model):
    events = models.ManyToManyField(
        Event, related_name='events', blank=True
    )
    areaOfOperations = models.ManyToManyField(
        AreaOfOperation, related_name='ao'
    )
