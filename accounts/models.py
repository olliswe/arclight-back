from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from rest_framework.authtoken.models import Token


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, first_name, last_name, password):
        """
        Creates and saves a staff user with the given email and password.
        """
        user = self.create_user(email, password=password)
        user.staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(email, password=password)
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(verbose_name="email address", max_length=255, unique=True)
    date_added = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)  # a admin user; non super-user
    admin = models.BooleanField(default=False)  # a superuser

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []  # Email & Password are required by default.

    def __str__(self):  # __unicode__ on Python 2
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, pih_app):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        return self.staff

    @property
    def is_admin(self):
        "Is the user a admin member?"
        return self.admin

    @property
    def is_active(self):
        "Is the user active?"
        return self.active

    objects = UserManager()


class UserProfile(models.Model):
    first_name = models.CharField(
        max_length=225, verbose_name="First Name", null=True, blank=True
    )
    last_name = models.CharField(
        max_length=225, verbose_name="Last Name", null=True, blank=True
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.email

    @receiver(post_save, sender=User)
    def create_or_update_user_profile(sender, instance, created, **kwargs):
        if created:
            UserProfile.objects.create(user=instance)
        instance.userprofile.save()
