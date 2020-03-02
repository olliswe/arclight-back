from rest_framework import views
from rest_framework import viewsets
from rest_framework.response import Response
from api.models import VideoUpload, Patient
from django.utils.dateparse import parse_datetime
from django.http import HttpResponseRedirect
import urllib
from .serializers import PatientSerializer


class FileUploadView(views.APIView):
    def post(self, request, format=None):
        file_obj = request.FILES["file"]
        file_obj.content_type = "video/mp4"
        name = request.POST["name"]
        dob = request.POST["dob"]
        dob_parsed = parse_datetime(dob)
        VideoUpload.objects.create(file=file_obj, name=name, dob=dob_parsed.date())
        # do some stuff with uploaded file
        return Response(status=204)


class PatientViewSet(viewsets.ModelViewSet):
    http_method_names = ["post", "patch"]
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer


def password_reset_redirect(request, redirect_url):
    scheme = urllib.parse.urlparse(redirect_url).scheme
    HttpResponseRedirect.allowed_schemes.append(scheme)
    return HttpResponseRedirect(redirect_url)
