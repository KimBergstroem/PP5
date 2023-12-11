from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver


class UserProfile(models.Model):
    """
    A extended user profile model for maintaining default
    delivery information and order history from allauth django user model
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Shipping detials
    default_phone_number = models.CharField(max_length=20, null=True, blank=True)
    default_country = CountryField(blank_label='Country', null=True, blank=True) 
    default_postcode = models.CharField(max_length=20, null=True, blank=True)
    default_town_or_city = models.CharField(max_length=40, null=True, blank=True)
    default_street_address1 = models.CharField(max_length=80, null=True, blank=True)
    default_street_address2 = models.CharField(max_length=80, null=True, blank=True)
    default_county = models.CharField(max_length=80, null=True, blank=True)
    
    # User's personal information
    first_name = models.CharField(max_length=20, blank=True)
    last_name = models.CharField(max_length=20, blank=True)
    email = models.EmailField(max_length=40, default="example@example.com")
    bio = models.TextField(
        max_length=150, default="Currently no bio", blank=True
        )
    profile_picture = models.ImageField(blank=True, upload_to='userprofile/', default="default_profile.png")
    country = models.CharField(
        max_length=30, default="Citizen of the Cyber world", blank=True
    )

    @receiver(post_save, sender=User)
    def create_or_update_user_profile(sender, instance, created, **kwargs):
        """
        Create or update the user profile
        """
        if created:
            UserProfile.objects.create(user=instance)
        # Existing users: just save the profile
        instance.userprofile.save()

    def get_date_joined(self):
        return self.user.date_joined

    def get_last_login(self):
        return self.user.last_login

    def __str__(self):
        return self.user.username
