from django.contrib.auth.models import AbstractUser
from django.contrib.postgres.fields import HStoreField
from django.conf import settings
from django.db import models

from social.models import SocialContacts


class UserNet(AbstractUser):
    """Custom User model for social-network 
    """
    middle_name = models.CharField(max_length=50, null=True)

    followers = models.ManyToManyField(
        to='self', null=True
    )

    @property
    def full_name(self):
        return f'{super().get_full_name()} {self.middle_name}'

class Profile(models.Model):
    """
    """
    GENDER = (
        ('male', 'male'),
        ('female', 'female'),
    )
    user = models.OneToOneField(
        to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile',
    )

    description = models.CharField(max_length=200, null=True)
    bio = models.TextField(null=True)
    gender = models.CharField(max_length=6, choices=GENDER, null=True)
    birthday = models.DateField(null=True)
    city = models.CharField(max_length=100, null=True)
    country = models.CharField(max_length=300, null=True)

class PrivacySettings(models.Model):
    """
    """
    HIDDEN_STATUS = (
        ('all', 'all'),
        ('confirmed', 'confirmed'),
        ('nobody', 'nobody'),
    )

    user = models.OneToOneField(
        to=Profile,  on_delete=models.CASCADE, related_name='privacy',
    )
    
    user_is_hidden = models.BooleanField(default=False) # Hidden user everywhere
    profile_is_hidden = models.BooleanField(default=False) # Hidden information on user profile
    activity_status_is_hidden = models.CharField(max_length=20, choices=HIDDEN_STATUS, default='all') # Hidden current status and time last login 

    hidden_fields = HStoreField(null=True, blank=True)
    
class UserAvatar(models.Model):
    """User image avatar, there may be several, only one is used
    """
    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='avatars'
    )
    using = models.BooleanField(default=True)
    image = models.ImageField(upload_to='user/avatars/')

class Follower(models.Model):
    """Subcribers and subscriptions for Users
    """
    RELATION = (
        ('not confirmed', 'not confirmed'),
        ('confirmed', 'confirmed'),
        ('blacklist', 'blacklist')
    )

    subscription = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='subscribers'
    )
    follower = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='subscriptions'
    )
    relation = models.CharField(max_length=20, choices=RELATION, default='not confirmed')

    def __str__(self) -> str:
        return f'{self.follower.username}:{self.subscription}'

    @property
    def subscription_url(self):
        return f'/api/user/{self.subscription}'

    @property
    def follower_url(self):
        return f'/api/user/{self.follower}/'
    
class UserContacts(models.Model):
    """Social contacts that users have
    """
    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='contacts'
    )
    social_contact = models.ForeignKey(
        to=SocialContacts, on_delete=models.SET_NULL, null=True
    )
    value = models.CharField(max_length=250)

    def __str__(self) -> str:
        return f'{self.user}:{self.social_contact} - {self.value}'

class Technology(models.Model):
    """Techologies in social-network
    """
    parent = models.ForeignKey(
        to='self', on_delete= models.SET_NULL, null=True, blank=True, related_name='childs'
    )
    name = models.CharField(max_length=200)
    url = models.SlugField(max_length=100)
    content = models.TextField(default='')
    confirmed = models.BooleanField(default=False)

    @property
    def absolute_url(self):
        return f"/api/technology/{self.url}/"

    def __str__(self) -> str:
        return f"{self.parent if self.parent else ''}:{self.name}"

class UserTechnology(models.Model):
    """Techologies that users have
    """
    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='skills'
    )
    technology = models.ForeignKey(
        to=Technology, on_delete=models.CASCADE
    )
    level = models.PositiveSmallIntegerField()
    experience = models.PositiveSmallIntegerField()

    def __str__(self) -> str:
        return f'{self.user}:{self.technology.name} - {self.level}/{self.experience}'