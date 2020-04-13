import graphene
from graphene_django.types import DjangoObjectType
from .models import Patient, VideoUpload, DoctorComment, ScreenerComment
from graphene_django_extras.fields import DjangoFilterListField
from accounts.models import Facility, User


class UserObjectType(DjangoObjectType):
    class Meta:
        model = User


class FacilityObjectType(DjangoObjectType):
    class Meta:
        model = Facility


class DoctorCommentObjectType(DjangoObjectType):
    class Meta:
        model = DoctorComment


class ScreenerCommentObjectType(DjangoObjectType):
    class Meta:
        model = ScreenerComment


class PatientObjectType(DjangoObjectType):
    age = graphene.String(source="age")

    class Meta:
        model = Patient
        filter_fields = {
            "full_name": ["exact", "icontains"],
            "facility__facility_name": ["exact", "icontains"],
        }


class VideoUploadObjectType(DjangoObjectType):
    signed_url = graphene.String(source="signed_url")
    signed_signature_url = graphene.String(source="signed_signature_url")

    class Meta:
        model = VideoUpload
        filter_fields = {
            "doctor_status": ["exact"],
            "screener_status": ["exact"],
            "id": ["exact"],
            "patient__full_name": ["icontains"],
        }


class Query(graphene.ObjectType):
    patient = graphene.Field(PatientObjectType, patient_id=graphene.String())
    my_patients = DjangoFilterListField(PatientObjectType)

    video_upload = graphene.Field(
        VideoUploadObjectType, video_upload_id=graphene.String()
    )
    all_video_uploads = DjangoFilterListField(VideoUploadObjectType)

    my_video_uploads = DjangoFilterListField(VideoUploadObjectType)

    def resolve_patient(self, info, patient_id):
        return Patient.objects.get(pk=patient_id)

    def resolve_my_patients(self, info, **kwargs):
        return Patient.objects.filter(facility=info.context.user.facility)

    def resolve_video_upload(self, info, video_upload_id):
        return VideoUpload.objects.get(pk=video_upload_id)

    def resolve_all_video_uploads(self, info, **kwargs):
        return VideoUpload.objects.all()

    def resolve_my_video_uploads(self, info, **kwargs):
        return VideoUpload.objects.filter(patient__facility=info.context.user.facility)
