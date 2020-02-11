from rest_framework import views
from rest_framework.response import Response
from api.models import VideoUpload
from django.utils.dateparse import parse_datetime
from django.http import HttpResponseRedirect
import urllib
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.decorators import api_view, parser_classes


class CsrfExemptSessionAuthentication(SessionAuthentication):
    def enforce_csrf(self, request):
        return  # To not perform the csrf check previously happening


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


def password_reset_redirect(request, redirect_url):
    scheme = urllib.parse.urlparse(redirect_url).scheme
    HttpResponseRedirect.allowed_schemes.append(scheme)
    return HttpResponseRedirect(redirect_url)
