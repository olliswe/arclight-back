from django.core.management.base import BaseCommand
from accounts.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        if not User.objects.filter(email="arclightmedical.app@gmail.com").exists():
            User.objects.create_superuser(
                "arclightmedical.app@gmail.com", "please_change_me"
            )
