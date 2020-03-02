from django.db import models
from django.utils.text import slugify
from datetime import datetime
from datetime import date, timedelta
from accounts.models import Facility


def upload_location_video(instance, filename):
    return "video_uploads/%s/%s" % (
        datetime.now().strftime("%d%m%Y"),
        filename.replace("MOV", "mp4"),
    )


class Patient(models.Model):
    GENDER_OPTIONS = [("male", "Male"), ("female", "Female")]
    full_name = models.CharField(verbose_name="Patient Name", max_length=1000)
    uid = models.CharField(verbose_name="Unique Identifier", max_length=50, unique=True)
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

    def age(self):
        return (date.today() - self.dob) // timedelta(days=365.2425)

    def __str__(self):
        return self.full_name + " (" + self.uid + ") "


class VideoUpload(models.Model):
    name = models.CharField(
        verbose_name="Patient Name", max_length=1000, null=True, blank=True
    )
    dob = models.DateField(verbose_name="Date of Birth", null=True, blank=True)
    file = models.FileField(upload_to=upload_location_video)
    date_recorded = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name + "   |  " + self.dob.strftime("%m/%d/%Y")
