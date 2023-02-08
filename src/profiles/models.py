from django.contrib.auth.models import AbstractUser

from django.db import models


class UserNet(AbstractUser):
    """ Custom User model for social-network """
    GENDER = (
        ('ml', 'male'),
        ('fm', 'female'),
    )

    middle_name = models.CharField(max_length=50, null=True)
    bio = models.TextField(null=True)
    gender = models.CharField(max_length=6, choices=GENDER, null=True)
    birthday = models.DateField(null=True)
    profile_is_hidden = models.BooleanField(default=False)
    
    followers = models.ManyToManyField(
        to='self', null=True
    )

    def get_full_name(self):
        return f'{super().get_full_name()} {self.middle_name}'

class Follower(models.Model):
    RELATION = (
        ('not confirmed', 'not confirmed'),
        ('confirmed', 'confirmed'),
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
    
class UserAvatar(models.Model):
    user = models.ForeignKey(
        to=UserNet, on_delete=models.CASCADE, related_name='avatars'
    )
    using = models.BooleanField(default=True)
    image = models.ImageField(upload_to='user/avatars/')

class SocialContacts(models.Model):
    name = models.CharField(max_length=150)
    icon = models.ImageField(upload_to='icon_social_account/')
    is_link = models.BooleanField()
    
class UserContacts(models.Model):
    user = models.ForeignKey(
        to=UserNet, on_delete=models.CASCADE, related_name='contacts'
    )
    social_contact = models.ForeignKey(
        to=SocialContacts, on_delete=models.SET_NULL, null=True
    )
    value = models.CharField(max_length=250)

class Technology(models.Model):
    parent = models.ForeignKey(
        to='self', on_delete= models.SET_NULL, null=True, related_name='childs'
    )
    name = models.CharField(max_length=200)

class UserTechnology(models.Model):
    user = models.ForeignKey(
        to=UserNet, on_delete=models.CASCADE, related_name='skils'
    )
    technology = models.ForeignKey(
        to=Technology, on_delete=models.CASCADE
    )
    level = models.PositiveSmallIntegerField()
    experience = models.PositiveSmallIntegerField()
