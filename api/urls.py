from django.urls import path
from . import views

urlpatterns = [path("upload_video/", views.FileUploadView.as_view())]
