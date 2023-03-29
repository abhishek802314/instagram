from rest_framework import serializers
from .models import User, UserImage

class UserImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserImage
        fields = '__all__'
        read_only_fields = ['user']


class UserAvatarSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserImage
        fields = ['image']
        

class UserSerializerList(serializers.ModelSerializer):
    user_image = UserAvatarSerializer(many=True, read_only=True)
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'last_action', 'is_online', 'is_private', 'hide_status', 'user_image']


class MySerializerList(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'is_private', 'hide_status']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'password']

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user