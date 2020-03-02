from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter
from .views import PatientViewSet

router = DefaultRouter()
router.register(r"patients", PatientViewSet, basename="patient")

urlpatterns = [
    path("upload_video/", views.FileUploadView.as_view()),
    path("password_reset_redirect/<path:redirect_url>/", views.password_reset_redirect),
]


urlpatterns += router.urls
