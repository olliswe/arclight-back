# Generated by Django 3.0.2 on 2020-02-13 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("api", "0002_auto_20200204_1244")]

    operations = [
        migrations.CreateModel(
            name="Patient",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "first_name",
                    models.CharField(
                        max_length=1000, verbose_name="Patient First Name"
                    ),
                ),
                (
                    "last_name",
                    models.CharField(max_length=1000, verbose_name="Patient Last Name"),
                ),
                (
                    "uid",
                    models.CharField(
                        max_length=50, unique=True, verbose_name="Unique Identifier"
                    ),
                ),
                ("dob", models.DateField(verbose_name="Date of Birth")),
                (
                    "gender",
                    models.CharField(
                        choices=[("male", "Male"), ("female", "Female")],
                        max_length=50,
                        verbose_name="Gender",
                    ),
                ),
                (
                    "telephone_number",
                    models.CharField(
                        blank=True,
                        max_length=1000,
                        null=True,
                        verbose_name="Telephone Number",
                    ),
                ),
            ],
        ),
        migrations.AlterField(
            model_name="videoupload",
            name="dob",
            field=models.DateField(blank=True, null=True, verbose_name="Date of Birth"),
        ),
        migrations.AlterField(
            model_name="videoupload",
            name="name",
            field=models.CharField(
                blank=True, max_length=1000, null=True, verbose_name="Patient Name"
            ),
        ),
    ]
