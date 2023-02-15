from django.db import models
from django.conf import settings

class AbstractComment(models.Model):
    """"""
    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comments'
    )
    parent = models.ForeignKey(
        'self', on_delete=models.SET_NULL, null=True, blank=True, related_name='childs'
    )
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class AbstractReaction(models.Model):
    EMOTION = (
        ('like', 'like'),
        ('dislike', 'dislike'),
        ('pog', 'pog'),
        ('fun', 'fun'),
    )
    
    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    )
    emotion = models.CharField(max_length=20, choices=EMOTION)

    class Meta:
        abstract = True

class SocialContacts(models.Model):
    """Social contacts
    """
    name = models.CharField(max_length=150)
    is_link = models.BooleanField()
    def __str__(self) -> str:
        return self.name