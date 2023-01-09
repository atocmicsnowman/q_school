from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField


class Pax(models.Model):
    """
    The user profile that extends a user object.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    f3_handle = models.CharField(max_length=80)
    cell_number = PhoneNumberField(blank=True, null=True)
    sms_subscribed = models.BooleanField(default=True)
    sms_notifications = models.BooleanField(default=True)
    email = models.EmailField()
    email_subscribed = models.BooleanField(default=True)
    email_notifications = models.BooleanField(default=True)
    retired = models.BooleanField(default=False)
    city = models.CharField(max_length=200, blank=True, null=True)


class SocialMediaPlatform(models.Model):
    """
    Twitter, FB, Slack, etc
    """
    platform_name = models.CharField(max_length=90)
    platform_site = models.URLField(blank=True, null=True)
    platform_target = models.URLField(blank=True, null=True)
    platform_android_link = models.URLField(blank=True, null=True)
    platform_ios_link = models.URLField(blank=True, null=True)
    details = models.TextField(blank=True, null=True)


class SocialMediaAccount(models.Model):
    """
    An social media account can be tied to a user or a platform. 
    
    A region-owned account does not need owner_pax to be populated, however it
    would be very helpful to have both in the instance that people need to 
    reach the controller(s)
    """
    owner_pax = models.ForeignKey(Pax, null=True, blank=True, on_delete=models.CASCADE)
    social_media_platform = models.ForeignKey(
        SocialMediaPlatform, on_delete=models.CASCADE
    )

