from django.db import models
from django.conf import settings

from social.models import AbstractComment, AbstractReaction
from profiles.models import UserNet, Technology


class Post(models.Model):
    """ Model for post """
    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='posts'
    )
    header = models.CharField(max_length=200)
    content = models.TextField()
    data = models.DateTimeField(auto_now_add=True, blank=True)
    published = models.BooleanField()
    number_of_views = models.PositiveBigIntegerField()
    tags = models.ManyToManyField(
        to=Technology, related_name='posts'
    )

    def __str__(self) -> str:
        return f'{self.user}:{self.header}'

class PostComment (AbstractComment):
    """"""
    post = models.ForeignKey(
        to=Post, on_delete=models.CASCADE, related_name='comments'
    )

    def __str__(self) -> str:
        return f'{self.post}:{self.content}'

class PostReaction(AbstractReaction):
    """"""
    post = models.ForeignKey(
        to=Post, on_delete=models.CASCADE, related_name='post_reactions'
    )

    def __str__(self) -> str:
        return f'{self.post}:{self.emotion}'

class CommentReaction(AbstractReaction):
    """"""
    comment = models.ForeignKey(
        to=PostComment, on_delete=models.CASCADE, related_name='comment_reactions'
    )

    def __str__(self) -> str:
        return f'{self.comment}:{self.emotion}'