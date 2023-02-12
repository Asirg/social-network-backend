from rest_framework import serializers

from wall.serializers import ListPostSerialier
from .models import (
    UserNet,
    UserAvatar,
    Technology,
    UserTechnology,
    SocialContacts,
    UserContacts,
    Follower,
)

class TechnologyParentSerializer(serializers.ModelSerializer):
    """
    """
    class Meta:
        model = Technology
        fields = ('name', 'absolute_url')

class TechnologySerializer(serializers.ModelSerializer):
    """
    """
    parent = TechnologyParentSerializer()
    class Meta:
        model = Technology
        fields = ('parent', 'name', 'absolute_url')

class RetrieveTechnologySerializer(serializers.ModelSerializer):
    """
    """
    class Meta:
        model = Technology
        fields = '__all__'

class UserTechnologySerializer(serializers.ModelSerializer):
    """ Serializer for user tecnologies 
    """
    technology = serializers.SlugRelatedField('name', read_only=True)
    class Meta:
        model = UserTechnology
        fields = ('technology', 'level', 'experience', )

class SocialContactsSerializer(serializers.ModelSerializer):
    """ Serializer for Social Contacts 
    """

    class Meta:
        model = SocialContacts
        fields = ('name', 'is_link', )

class UserContactsSerializer(serializers.ModelSerializer):
    """ Serializer for Social Contacts for user 
    """
    social_contact = SocialContactsSerializer(read_only=True)

    class Meta:
        model = UserContacts
        fields = ('social_contact', 'social_contact', )

class FilterUsingAvatar(serializers.ListSerializer):
    """ Filter by get only using Users avatars 
    """
    def to_representation(self, data):
        data = data.filter(using=True)
        return super().to_representation(data)

class UserAvatarSerializer(serializers.ModelSerializer):
    """ Serializer for user avatar 
    """
    class Meta:
        model = UserAvatar
        fields = ('image', 'using', )
    
class UsingUserAvatarSerializer(serializers.ModelSerializer):
    """ Serializer for using user avatar 
    """
    class Meta:
        model = UserAvatar
        list_serializer_class = FilterUsingAvatar
        fields = ('image', 'using', )

class UserSerializer(serializers.ModelSerializer):
    """ Serializer for users in network
    """
    avatars = UsingUserAvatarSerializer(many=True)

    class Meta:
        model = UserNet
        fields = (
            'id',
            'avatars', 
            'username',
            'description',
            'last_login', 
        )

class RetrieveUserSerializer(serializers.ModelSerializer):
    """ Serializer for detail informations about users
    """
    avatars = UserAvatarSerializer(many=True, read_only=True)
    contacts = UserContactsSerializer(many=True, read_only=True)

    last_login = serializers.ReadOnlyField()
    date_joined = serializers.ReadOnlyField()
    
    class Meta:
        model = UserNet
        fields = (
            'username', 'description', 'first_name', 'middle_name', 'last_name',
            'gender', 'bio', 'birthday', 'city', 'country',
            'contacts', 'avatars',
            'date_joined', 'last_login',
        )

class UpdateUserSerializer(serializers.ModelSerializer):
    """ Serializer for detail informations about users
    """
    
    class Meta:
        model = UserNet
        fields = (
            'username', 'description', 'first_name', 'middle_name', 'last_name',
            'gender', 'bio', 'birthday', 'city', 'country',
            'user_is_hidden', 
            'profile_is_hidden', 
            'chat_is_closed', 
            'personal_information_is_hidden', 
            'activity_status_is_hidden',
        )

class FollowerSerializer(serializers.ModelSerializer):
    """
    """
    
    class Meta:
        model = Follower
        fields = (
            'id', 'relation', 'subscription_url', 'follower_url'
        )