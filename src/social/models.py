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
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class ReactionEmotion(models.Model):
    EMOTION = (
        ('like', 'like'),
        ('dislike', 'dislike'),
        ('pog', 'pog'),
        ('fun', 'fun'),
    )
    emotion = models.CharField(max_length=20, choices=EMOTION)
    icon = models.ImageField(upload_to='emotion_icons/')

class AbstractReaction(models.Model):
    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    )
    emotion = models.ForeignKey(
        to=ReactionEmotion, on_delete=models.CASCADE
    )

    class Meta:
        abstract = True
