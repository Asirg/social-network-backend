from rest_framework import serializers

from wall.serializers import ListPostSerialier
from social.serializers import SocialContactsSerializer
from utility.services import check_user_privacy
from .models import (
    UserAvatar,
    Profile,
    PrivacySettings,
    UserNet,
    
    
    Technology,
    UserTechnology,
    SocialContacts,
    UserContacts,
    Follower,
)
class UsingUserAvatarSerializer(serializers.BaseSerializer):
    """ Serializer for get using user Avatar
    """
    def to_representation(self, instance):
        return instance.get(using=True).image.url

class UserSerializer(serializers.ModelSerializer):
    """ Serializer for users in network
    """
    avatars = UsingUserAvatarSerializer()

    class Meta:
        model = UserNet
        fields = ('id', 'avatars', 'username', 'description', 'last_login')

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        exclude = ('id', 'user')
        
    def to_representation(self, instance):
        data = super().to_representation(instance)
        hidden_fields = instance.privacy.get_hidden_fields(
                check_user_privacy(instance.user, self.context['request'].user)
        )
        return {
            key:value for key, value in data.items() \
                if key not in hidden_fields
        }

class RetrieveUserSerializer(serializers.ModelSerializer):
    """ Serializer for detail informations about users
    """
    profile = UserProfileSerializer()

    last_login = serializers.ReadOnlyField()
    
    class Meta:
        model = UserNet
        fields = ('id', 'avatars', 'username', 'description', 'last_login', 'profile',)



class UsingUserAvatarSerializer(serializers.ModelSerializer):
    """ Serializer for using user avatar 
    """
    class Meta:
        model = UserAvatar
        fields = ('image', 'using', )

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

class UserContactsSerializer(serializers.ModelSerializer):
    """ Serializer for Social Contacts for user 
    """
    social_contact = SocialContactsSerializer(read_only=True)

    class Meta:
        model = UserContacts
        fields = ('social_contact', 'social_contact', )


class FollowerSerializer(serializers.ModelSerializer):
    """
    """
    
    class Meta:
        model = Follower
        fields = (
            'id', 'relation', 'subscription_url', 'follower_url'
        )