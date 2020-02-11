from django.db import models
from django.utils.text import slugify
from datetime import datetime


def upload_location_video(instance, filename):
    return "video_uploads/%s/%s" % (
        datetime.now().strftime("%b-%Y"),
        filename.replace("MOV", "mp4"),
    )


class VideoUpload(models.Model):
    name = models.CharField(
        verbose_name="Patient Name", max_length=1000, null=True, blank=True
    )
    dob = models.DateField(verbose_name="Date of Birth", null=True, blank=True)
    file = models.FileField(upload_to=upload_location_video)

    def __str__(self):
        return self.name + "   |  " + self.dob.strftime("%m/%d/%Y")
