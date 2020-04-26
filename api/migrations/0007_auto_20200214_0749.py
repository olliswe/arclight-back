# Generated by Django 3.0.2 on 2020-02-14 07:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0006_auto_20200213_1629"),
        ("api", "0006_auto_20200213_1645"),
    ]

    operations = [
        migrations.AlterField(
            model_name="patient",
            name="facility",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="accounts.Facility",
            ),
        )
    ]