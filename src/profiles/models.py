from django.contrib.auth.models import AbstractUser
from django.contrib.postgres.fields import HStoreField
from django.conf import settings
from django.db import models

from social.models import SocialContacts
from skills.models import Technology


class UserNet(AbstractUser):
    """Custom User model for social-network 
    """
    middle_name = models.CharField(max_length=50, null=True)
    description = models.CharField(max_length=200, null=True)

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

    bio = models.TextField(null=True, blank=True)
    gender = models.CharField(max_length=6, choices=GENDER, null=True, blank=True)
    birthday = models.DateField(null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    country = models.CharField(max_length=300, null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.user.username}:{self.user.id}"

class PrivacySettings(models.Model):
    """
    """
    HIDDEN_STATUS = (
        ('all', 'all'),
        ('confirmed', 'confirmed'),
        ('nobody', 'nobody'),
    )

    profile = models.OneToOneField(
        to=Profile,  on_delete=models.CASCADE, related_name='privacy',
    )
    
    user_is_hidden = models.BooleanField(default=False) # Hidden user everywhere
    profile_is_hidden = models.BooleanField(default=False) # Hidden information on user profile
    # activity_status_is_hidden = models.CharField(max_length=20, choices=HIDDEN_STATUS, default='all') # Hidden current status and time last login 

    hidden_fields = HStoreField(null=True, blank=True)

    def __check_privacy__(self, privacy, level):
        return self.HIDDEN_STATUS.index((level, level)) < self.HIDDEN_STATUS.index((privacy, privacy))

    def get_hidden_fields(self, level):
        return [
            field for field, privacy in self.hidden_fields.items() \
                if self.__check_privacy__(privacy, level)
        ]

    def __str__(self) -> str:
        return self.profile.user.username
    
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