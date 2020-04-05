from django.contrib import admin
from .models import VideoUpload, Patient, DoctorComment, ScreenerComment


admin.site.register(VideoUpload)
admin.site.register(Patient)
admin.site.register(DoctorComment)
admin.site.register(ScreenerComment)
