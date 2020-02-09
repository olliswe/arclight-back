from django.urls import path
from . import views

urlpatterns = [
    path("upload_video/", views.FileUploadView.as_view()),
    path("password_reset_redirect/<path:redirect_url>/", views.password_reset_redirect),
]
