from django.contrib import admin

from wall.models import (
    Post,
    PostComment,
    PostReaction,
    CommentReaction,
)

admin.site.register(Post)
admin.site.register(PostComment)
admin.site.register(PostReaction)
admin.site.register(CommentReaction)