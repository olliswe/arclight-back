# Generated by Django 3.0.2 on 2020-02-13 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("api", "0005_auto_20200213_1641")]

    operations = [
        migrations.RemoveField(model_name="patient", name="first_name"),
        migrations.RemoveField(model_name="patient", name="last_name"),
        migrations.AddField(
            model_name="patient",
            name="full_name",
            field=models.CharField(
                default="test", max_length=1000, verbose_name="Patient Name"
            ),
            preserve_default=False,
        ),
    ]
