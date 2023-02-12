from django.db import models
from django.conf import settings
from django.db.models import Count

from social.models import AbstractComment, AbstractReaction
from profiles.models import UserNet, Technology


class Post(models.Model):
    """ Model for post """
    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='posts'
    )
    header = models.CharField(max_length=200)
    content = models.TextField()
    published = models.BooleanField(default=True)
    published_date = models.DateTimeField(auto_now_add=True, blank=True)
    number_of_views = models.PositiveBigIntegerField(default=0)
    tags = models.ManyToManyField(
        to=Technology, related_name='posts'
    )

    @property
    def comment_count(self):
        return self.comments.all().count()

    @property
    def reactions_count(self):
        return Post.objects.get(pk=1)\
                            .reactions.all()\
                            .values('emotion')\
                            .annotate(count = Count('emotion'))
                            
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
        to=Post, on_delete=models.CASCADE, related_name='reactions'
    )

    def __str__(self) -> str:
        return f'{self.post}:{self.emotion}'

class CommentReaction(AbstractReaction):
    """"""
    comment = models.ForeignKey(
        to=PostComment, on_delete=models.CASCADE, related_name='reactions'
    )

    def __str__(self) -> str:
        return f'{self.comment}:{self.emotion}'