from rest_framework import serializers

from .models import UserNet

class ListUserNetSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserNet
        fields = (
            'id', 'is_active', 'username',
        )
    
class RetrieveUserNetSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserNet
        fields = (
            'id', 'last_login', 'username', 'first_name', 'last_name', 'email', 'date_joined', 'bio', 'gender', 'birthday',
        )

class CreateUserNetSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        user = UserNet(
            **validated_data
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

    class Meta:
        model = UserNet
        fields = (
            'username', 'password',
        )