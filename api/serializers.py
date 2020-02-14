from rest_framework import serializers
from .models import VideoUpload, Patient


class VideoUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoUpload
        fields = "__all__"


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = "__all__"

    def create(self, validated_data):
        validated_data["facility"] = self.context["request"].user.facility
        return super(PatientSerializer, self).create(validated_data)
