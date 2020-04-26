# Generated by Django 3.0.2 on 2020-02-13 16:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [("accounts", "0003_auto_20200213_1614")]

    operations = [
        migrations.AlterField(
            model_name="facility",
            name="user",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        )
    ]