from rest_framework import serializers

from wall.serializers import ListPostSerialier
from .models import (
    UserNet,
    UserAvatar,
    Technology,
    UserTechnology,
    SocialContacts,
    UserContacts,
)

class FilterUsingAvatar(serializers.ListSerializer):
    """ Filter by get only using Users avatars """
    def to_representation(self, data):
        data = data.filter(using=True)
        return super().to_representation(data)

class UserAvatarSerializer(serializers.ModelSerializer):
    """ Serializer for user avatar """
    class Meta:
        model = UserAvatar
        list_serializer_class = FilterUsingAvatar
        fields = ('image', 'using', )
        
class UserTechnologySerializer(serializers.ModelSerializer):
    """ Serializer for user tecnologies """
    technology = serializers.SlugRelatedField('name', read_only=True)
    class Meta:
        model = UserTechnology
        fields = ('technology', 'level', 'experience', )

class SocialContactsSerializer(serializers.ModelSerializer):
    """ Serializer for Social Contacts """
    class Meta:
        model = SocialContacts
        fields = ('name', 'is_link', )

class UserContactsSerializer(serializers.ModelSerializer):
    """ Serializer for Social Contacts for user """
    social_contact = SocialContactsSerializer(read_only=True)
    class Meta:
        model = UserContacts
        fields = ('social_contact', 'social_contact', )

class ListUserNetSerializer(serializers.ModelSerializer):
    """ Serializer for explain list users """
    avatars = UserAvatarSerializer(many=True)
    class Meta:
        model = UserNet
        fields = (
            'id', 'username', 'avatars',
        )

class RetrieveUserNetHiddenSerializer(serializers.ModelSerializer):
    """ Serializer for hidden profiles users """
    avatars = UserAvatarSerializer(many=True)
    class Meta:
        model = UserNet
        fields = (
            'username', 'avatars',
        )
class RetrieveUserNetSerializer(serializers.ModelSerializer):
    """ Serializer for public profiles users """
    avatars = UserAvatarSerializer(many=True)
    skills = UserTechnologySerializer(many=True)
    contacts = UserContactsSerializer(many=True)
    posts = ListPostSerialier(many=True)
    class Meta:
        model = UserNet
        fields = (
            'username', 'avatars', 'description',
            'gender', 'first_name', 'middle_name', 'last_name', 
            'last_login', 
            'bio', 'birthday', 
            'email', 
            'date_joined',
            'skills', 'contacts',
            'posts',
        )