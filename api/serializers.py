from rest_framework import serializers
from .models import VideoUpload, Patient, DoctorComment, ScreenerComment


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


class DoctorCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctorComment
        fields = "__all__"

    def create(self, validated_data):
        print("creating")
        videoupload_instance = validated_data["videoupload"]
        videoupload_instance.doctor_status = "archived"
        videoupload_instance.screener_status = "reviewed"
        videoupload_instance.save()
        return super(DoctorCommentSerializer, self).create(validated_data)


class ScreenerCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScreenerComment
        fields = "__all__"

    def create(self, validated_data):
        videoupload_instance = validated_data["videoupload"]
        videoupload_instance.doctor_status = "reopened"
        videoupload_instance.screener_status = "pending_review"
        videoupload_instance.save()
        return super(ScreenerCommentSerializer, self).create(validated_data)
