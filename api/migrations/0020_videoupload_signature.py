# Generated by Django 3.0.2 on 2020-04-12 16:34

import api.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("api", "0019_auto_20200403_0905")]

    operations = [
        migrations.AddField(
            model_name="videoupload",
            name="signature",
            field=models.FileField(
                null=True, upload_to=api.models.upload_location_image
            ),
        )
    ]
