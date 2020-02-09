from django.shortcuts import render
from rest_framework import views
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from api.models import VideoUpload
from django.utils.dateparse import parse_datetime
from django.http import HttpResponseRedirect
import urllib


class FileUploadView(views.APIView):
    parser_classes = (MultiPartParser,)

    def post(self, request, format=None):
        print(request.POST)
        print(request.FILES)
        file_obj = request.FILES["file"]
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
