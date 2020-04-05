from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter
from .views import PatientViewSet, DoctorCommentViewSet, ScreenerCommentViewSet

router = DefaultRouter()
router.register(r"patients", PatientViewSet, basename="patient")
router.register(r"doctor_comments", DoctorCommentViewSet, basename="doctor_comments")
router.register(
    r"screener_comments", ScreenerCommentViewSet, basename="screener_comments"
)


urlpatterns = [
    path("upload_video/", views.FileUploadView.as_view()),
    path("password_reset_redirect/<path:redirect_url>/", views.password_reset_redirect),
    path("archive_video/<int:id>/", views.archiveVideo),
]


urlpatterns += router.urls
