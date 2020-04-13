from django.db import models
from datetime import datetime
from datetime import date, timedelta
from accounts.models import Facility, User
from django.utils.text import slugify


def upload_location_video(instance, filename):
    return "screenings/%s/Patient_ID_%s/%s_video.mp4" % (
        slugify(instance.patient.facility.facility_name),
        str(instance.patient.id),
        datetime.now().strftime("%d%m%Y_%H%M"),
    )


def upload_location_image(instance, filename):
    return "screenings/%s/Patient_ID_%s/%s_signature.png" % (
        slugify(instance.patient.facility.facility_name),
        str(instance.patient.id),
        datetime.now().strftime("%d%m%Y_%H%M"),
    )


class Patient(models.Model):
    GENDER_OPTIONS = [("Male", "Male"), ("Female", "Female")]
    full_name = models.CharField(verbose_name="Patient Name", max_length=1000)
    dob = models.DateField(verbose_name="Date of Birth")
    gender = models.CharField(
        verbose_name="Gender", choices=GENDER_OPTIONS, max_length=50
    )
    telephone_number = models.CharField(
        verbose_name="Telephone Number", max_length=1000, null=True, blank=True
    )
    facility = models.ForeignKey(
        Facility, on_delete=models.CASCADE, null=True, blank=True
    )

    @property
    def age(self):
        return (date.today() - self.dob) // timedelta(days=365.2425)

    def __str__(self):
        return self.full_name


class VideoUpload(models.Model):
    DOCTOR_STATUS_OPTIONS = [
        ("new", "New"),
        ("reopened", "Reopened"),
        ("archived", "Archived"),
    ]
    SCREENER_STATUS_OPTIONS = [
        ("pending_review", "Pending Review"),
        ("reviewed", "Reviewed"),
        ("archived", "Archived"),
    ]
    file = models.FileField(upload_to=upload_location_video)
    signature = models.FileField(upload_to=upload_location_image, null=True)
    date_recorded = models.DateField(auto_now_add=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    comment = models.TextField(verbose_name="Comment", default="")
    under_review_by_doctor = models.BooleanField(
        verbose_name="Under Review by Doctor", default=False
    )
    doctor_status = models.CharField(
        verbose_name="Doctor's Status",
        choices=DOCTOR_STATUS_OPTIONS,
        default="new",
        max_length=50,
    )
    screener_status = models.CharField(
        verbose_name="Screener's Status",
        choices=SCREENER_STATUS_OPTIONS,
        default="pending_review",
        max_length=50,
    )

    @property
    def signed_url(self):
        return self.file.url

    @property
    def signed_signature_url(self):
        return self.signature.url

    def __str__(self):
        return self.patient.full_name + "   |  " + self.patient.dob.strftime("%m/%d/%Y")


class DoctorComment(models.Model):
    comment = models.TextField(verbose_name="Diagnosis Comment")
    videoupload = models.ForeignKey(
        VideoUpload, on_delete=models.CASCADE, related_name="doctor_comments"
    )
    date_added = models.DateTimeField(auto_now_add=True)
    physician = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True
    )

    class Meta:
        ordering = ["-date_added", "-id"]


class ScreenerComment(models.Model):
    comment = models.TextField(verbose_name="Screener Comment")
    videoupload = models.ForeignKey(
        VideoUpload, on_delete=models.CASCADE, related_name="screener_comments"
    )
    date_added = models.DateTimeField(auto_now_add=True)
    screener = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
