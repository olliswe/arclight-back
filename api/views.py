from django.shortcuts import render
from rest_framework import views
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from api.models import VideoUpload


class FileUploadView(views.APIView):
    parser_classes = (MultiPartParser,)

    def post(self, request, format=None):
        print(request.POST)
        print(request.FILES)
        file_obj = request.FILES["file"]
        VideoUpload.objects.create(file=file_obj)
        # do some stuff with uploaded file
        return Response(status=204)
