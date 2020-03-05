# Generated by Django 3.0.2 on 2020-03-02 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("api", "0007_auto_20200214_0749")]

    operations = [
        migrations.RemoveField(model_name="videoupload", name="patient"),
        migrations.AddField(
            model_name="videoupload",
            name="dob",
            field=models.DateField(blank=True, null=True, verbose_name="Date of Birth"),
        ),
        migrations.AddField(
            model_name="videoupload",
            name="name",
            field=models.CharField(
                blank=True, max_length=1000, null=True, verbose_name="Patient Name"
            ),
        ),
    ]
