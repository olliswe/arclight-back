from rest_framework import views
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from api.models import VideoUpload, Patient, DoctorComment, ScreenerComment
from django.http import HttpResponseRedirect
import urllib
from .serializers import (
    PatientSerializer,
    DoctorCommentSerializer,
    ScreenerCommentSerializer,
)


class FileUploadView(views.APIView):
    def post(self, request, format=None):
        print(request.FILES)
        file_obj = request.FILES["file"]
        file_obj.content_type = "video/mp4"
        patient_id = request.POST["patient_id"]
        patient = Patient.objects.get(id=int(patient_id))
        comment = request.POST["comment"]
        VideoUpload.objects.create(file=file_obj, patient=patient, comment=comment)
        return Response(status=204)


class PatientViewSet(viewsets.ModelViewSet):
    http_method_names = ["post", "patch"]
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer


class DoctorCommentViewSet(viewsets.ModelViewSet):
    http_method_names = ["post", "patch"]
    queryset = DoctorComment.objects.all()
    serializer_class = DoctorCommentSerializer


class ScreenerCommentViewSet(viewsets.ModelViewSet):
    http_method_names = ["post", "patch"]
    queryset = ScreenerComment.objects.all()
    serializer_class = ScreenerCommentSerializer


def password_reset_redirect(request, redirect_url):
    scheme = urllib.parse.urlparse(redirect_url).scheme
    HttpResponseRedirect.allowed_schemes.append(scheme)
    return HttpResponseRedirect(redirect_url)


@api_view(["PATCH"])
def archiveVideo(request, id):
    videoInstance = VideoUpload.objects.get(id=id)
    videoInstance.screener_status = "archived"
    videoInstance.save()
    return Response("Success")
