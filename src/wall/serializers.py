from rest_framework import serializers

from utility.serializers import RecursiveSerializer, FilterCommentListSerializer
from wall.models import (
    Post,
    PostComment,
    PostReaction,
    CommentReaction,
)


class PostCommentSerializer(serializers.ModelSerializer):
    childs = RecursiveSerializer(many=True)

    class Meta:
        model = PostComment
        list_serializer_class = FilterCommentListSerializer
        fields = ('user', 'content', 'created_date', 'updated_date', 'childs')

class PostReactionSerializers(serializers.ModelSerializer):
    """
    """

    class Meta:
        model = PostReaction
        fields = '__all__'

class CommentReactionSerializers(serializers.ModelSerializer):
    """
    """

    class Meta:
        model = CommentReaction
        fields = '__all__'


class ListPostSerialier(serializers.ModelSerializer):
    """
    """
    user = serializers.StringRelatedField()
    tags = serializers.SlugRelatedField('name', many=True, read_only=True)
    comment_count = serializers.ReadOnlyField()
    reactions_count = serializers.ReadOnlyField()

    class Meta:
        model = Post
        exclude = (
            'content', 'id', 'published'
        )

class RetrievePostSerializer(serializers.ModelSerializer):
    """
    """
    user = serializers.ReadOnlyField(source='username')
    tags = serializers.SlugRelatedField('name', many=True, read_only=True)
    comment_count = serializers.ReadOnlyField()
    reactions_count = serializers.ReadOnlyField()

    class Meta:
        model = Post
        fields = '__all__'