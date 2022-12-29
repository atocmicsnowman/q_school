from django.db import models
from django_countries.fields import CountryField

from q_school.registration.models import Pax


class Region(models.Model):
    """
    A region is a grouping of F3 AOs that has its own local leadership teams,
    often referred to as the SLT (Shared Leadership Team) 
    """
    name = models.CharField(max_length=80)
    associated_city = models.CharField(max_length=200, blank=True, null=True)
    associated_country = CountryField()
    associated_territory = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    nantan = models.ForeignKey(
        Pax, related_name="region_nantan", 
        null=True, 
        blank=True, 
        on_delete=models.DO_NOTHING)
    weasel_shaker = models.ForeignKey(
        Pax,  related_name="region_weasel_shaker",
        null=True, 
        blank=True, 
        on_delete=models.DO_NOTHING)
    members = models.ManyToManyField(
        Pax,
        related_name='region_members'
    )

class AreaOfOperation(models.Model):
    """
    Area of Operation (AO, or Site) is the place where a group of PAX meets, it
    is not tied to any specific day, week, or time for workouts.
    """
    name = models.CharField(max_length=80)
    primary_site_q = models.ForeignKey(Pax, on_delete=models.DO_NOTHING, related_name='site_q')
    site_qs = models.ManyToManyField(Pax, related_name='site_committee')
    gps_long = models.DecimalField(max_digits=22, decimal_places=16)
    gps_lat = models.DecimalField(max_digits=22, decimal_places=16)
    street_address = models.CharField(max_length=240)
    street_address2 = models.CharField(max_length=240)
    country = CountryField()
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)
    