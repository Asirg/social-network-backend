from rest_framework import serializers

from utility.serializers import RecursiveSerializer, FilterCommentListSerializer
from social.serializers import ReactionEmotion
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
    emotion = ReactionEmotion()

    class Model:
        model = PostReaction
        fields = '__all__'

class CommentReactionSerializers(serializers.ModelSerializer):
    """
    """
    emotion = ReactionEmotion()

    class Model:
        model = CommentReaction
        list_serializer_class = FilterCommentListSerializer
        fields = '__all__'

class ListPostSerialier(serializers.ModelSerializer):
    """
    """
    user = serializers.SlugRelatedField('username', read_only=True)
    tags = serializers.SlugRelatedField('name', many=True, read_only=True)
    reactions = PostReactionSerializers(many=True)
    # comments = PostCommentSerializer(many=True)

    class Meta:
        model = Post
        exclude = (
            'content', 'id', 'published'
        )

class RetrievePostSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField('username', read_only=True)
    tags = serializers.SlugRelatedField('name', many=True, read_only=True)
    reactions = PostReactionSerializers(many=True)
    comments = PostCommentSerializer(many=True)

    class Meta:
        model = Post
        fields = '__all__'