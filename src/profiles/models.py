from django.contrib.auth.models import AbstractUser

from django.db import models


class UserNet(AbstractUser):
    """Custom User model for social-network 
    """
    GENDER = (
        ('male', 'male'),
        ('female', 'female'),
    )
    HIDDEN_STATUS = (
        ('all', 'all'),
        ('confirmed', 'confirmed'),
        ('nobody', 'nobody'),
    )

    followers = models.ManyToManyField(
        to='self', null=True
    )

    # about user
    middle_name = models.CharField(max_length=50, null=True)
    description = models.CharField(max_length=200, null=True)

    bio = models.TextField(null=True)
    gender = models.CharField(max_length=6, choices=GENDER, null=True)
    birthday = models.DateField(null=True)
    city = models.CharField(max_length=100, null=True)
    country = models.CharField(max_length=300, null=True)

    # confidentiality
    user_is_hidden = models.BooleanField(default=False) # Hidden user everywhere
    profile_is_hidden = models.BooleanField(default=False) # Hidden information on user profile
    chat_is_closed = models.CharField(max_length=20, choices=HIDDEN_STATUS, default='all') # Close send message
    personal_information_is_hidden = models.CharField(max_length=20, choices=HIDDEN_STATUS, default='all') # Hidded person information
    activity_status_is_hidden = models.CharField(max_length=20, choices=HIDDEN_STATUS, default='all') # Hidden current status and time last login 

    def __str__(self) -> str:
        return self.username

    @property
    def full_name(self):
        return f'{super().get_full_name()} {self.middle_name}'

class UserAvatar(models.Model):
    """User image avatar, there may be several, only one is used
    """
    user = models.ForeignKey(
        to=UserNet, on_delete=models.CASCADE, related_name='avatars'
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
        to=UserNet, on_delete=models.CASCADE, related_name='subscribers'
    )
    follower = models.ForeignKey(
        to=UserNet, on_delete=models.CASCADE, related_name='subscriptions'
    )
    relation = models.CharField(max_length=20, choices=RELATION, default='not confirmed')

    def __str__(self) -> str:
        return f'{self.follower.username}:{self.subscription}'

class SocialContacts(models.Model):
    """Social contacts
    """
    name = models.CharField(max_length=150)
    is_link = models.BooleanField()
    def __str__(self) -> str:
        return self.name
    
class UserContacts(models.Model):
    """Social contacts that users have
    """
    user = models.ForeignKey(
        to=UserNet, on_delete=models.CASCADE, related_name='contacts'
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

    def __str__(self) -> str:
        return f"{self.parent if self.parent else ''}:{self.name}"

class UserTechnology(models.Model):
    """Techologies that users have
    """
    user = models.ForeignKey(
        to=UserNet, on_delete=models.CASCADE, related_name='skills'
    )
    technology = models.ForeignKey(
        to=Technology, on_delete=models.CASCADE
    )
    level = models.PositiveSmallIntegerField()
    experience = models.PositiveSmallIntegerField()

    def __str__(self) -> str:
        return f'{self.user}:{self.technology.name} - {self.level}/{self.experience}'