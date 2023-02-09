from rest_framework import serializers

from .models import ReactionEmotion


class ReactionEmoutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReactionEmotion
        fields = '__all__'