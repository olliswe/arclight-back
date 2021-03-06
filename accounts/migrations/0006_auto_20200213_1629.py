# Generated by Django 3.0.2 on 2020-02-13 16:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [("accounts", "0005_auto_20200213_1626")]

    operations = [
        migrations.RemoveField(model_name="facility", name="user"),
        migrations.AddField(
            model_name="user",
            name="facility",
            field=models.OneToOneField(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="accounts.Facility",
            ),
        ),
        migrations.AlterField(
            model_name="facility",
            name="facility_country",
            field=models.CharField(
                default="Test", max_length=225, verbose_name="Facility Country"
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="facility",
            name="facility_name",
            field=models.CharField(
                default="Test", max_length=225, verbose_name="Facility Name"
            ),
            preserve_default=False,
        ),
    ]
