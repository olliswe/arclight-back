# Generated by Django 3.0.2 on 2020-03-15 16:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [("accounts", "0006_auto_20200213_1629")]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="facility",
            field=models.OneToOneField(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="facility",
                to="accounts.Facility",
            ),
        )
    ]
