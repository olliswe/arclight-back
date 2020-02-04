# Generated by Django 3.0.2 on 2020-02-04 12:44

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [("api", "0001_initial")]

    operations = [
        migrations.AddField(
            model_name="videoupload",
            name="dob",
            field=models.DateField(
                default=datetime.datetime(2020, 2, 4, 12, 44, 15, 517215, tzinfo=utc),
                verbose_name="Date of Birth",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="videoupload",
            name="name",
            field=models.CharField(
                default="Oliver", max_length=1000, verbose_name="Patient Name"
            ),
            preserve_default=False,
        ),
    ]
