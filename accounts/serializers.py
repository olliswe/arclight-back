from rest_framework import serializers
from .models import User, UserProfile


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ["first_name", "last_name"]


class UserSerializer(serializers.ModelSerializer):
    userprofile = UserProfileSerializer(many=False)

    class Meta:
        model = User
        fields = ("id", "email", "userprofile", "date_added", "password")
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        password = validated_data.pop("password")
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user

    def update(self, instance, validated_data):
        instance.email = validated_data.get("email", instance.email)
        instance.save()
        return instance
