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
    first_f = models.ForeignKey(
        Pax,  related_name="region_1st_f",
        null=True, 
        blank=True, 
        on_delete=models.DO_NOTHING)
    second_f = models.ForeignKey(
        Pax,  related_name="region_2nd_f",
        null=True, 
        blank=True, 
        on_delete=models.DO_NOTHING)
    third_f = models.ForeignKey(
        Pax,  related_name="region_3rd_f",
        null=True, 
        blank=True, 
        on_delete=models.DO_NOTHING)
    comz_team = models.ManyToManyField(
        Pax,
        related_name='region_comz_members'
    )
    members = models.ManyToManyField(
        Pax,
        related_name='region_members'
    )


class AreaOfOperationType(models.Model):
    """
    Definitions for AO type. Not using choices in AreaOfOperation so we can
    easily expand possibile types.
    """

    ao_type = models.CharField(max_length=80)


class AreaOfOperationFlavor(models.Model):
    """
    definitions for AO flavor. Basically, what typically happens at this AO

    Flavors should be, as a rule, VERY concise. No more than one or two
    words. Migrations will include the following default entries:
    Boot Camp, Gear, Moderate, Ruck, Run
    """
    ao_flavor = models.CharField(max_length=64)
    retired = models.BooleanField(default=False)


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
    city = models.CharField(max_length=120)
    state = models.CharField(max_length=120)
    country = CountryField()
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)
    ao_type = models.ForeignKey(
        AreaOfOperationType,
        on_delete=models.DO_NOTHING
        )
    ao_flavors = models.ManyToManyField(
        AreaOfOperationFlavor,
        related_name='ao_flavors'
    )
    