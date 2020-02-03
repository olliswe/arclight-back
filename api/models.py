from django.db import models
from django.utils.text import slugify
from datetime import datetime


def upload_location_video(instance, filename):
    return "video_uploads/%s/%s" % (datetime.now().strftime("%b-%Y"), instance.id)


class VideoUpload(models.Model):
    file = models.FileField(upload_to=upload_location_video)
