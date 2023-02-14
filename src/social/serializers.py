from rest_framework import serializers

from .models import SocialContacts

class SocialContactsSerializer(serializers.ModelSerializer):
    """ Serializer for Social Contacts 
    """

    class Meta:
        model = SocialContacts
        fields = ('name', 'is_link', )