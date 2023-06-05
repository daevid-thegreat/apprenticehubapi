from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.utils import timezone
from apprenticehubapi.settings import AUTH_USER_MODEL

User = AUTH_USER_MODEL


class Company(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    website = models.CharField(max_length=100)
    industry = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    facebook = models.CharField(max_length=100)
    twitter = models.CharField(max_length=100)
    linkedin = models.CharField(max_length=100)
    instagram = models.CharField(max_length=100)

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class OTP(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    otp = models.CharField(max_length=6)
    is_used = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)


    def is_expired(self):
        if self.created_at + timezone.timedelta(minutes=60) <= timezone.now():
            return True

    def __str__(self):
        return self.otp


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(email=email, password=password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Userprofile(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=150)
    email = models.EmailField(max_length=100, unique=True)

    tel = models.CharField(max_length=100)

    is_master = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'

    objects = CustomUserManager()

    def __str__(self):
        return self.email


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class Apprentice(models.Model):
    user = models.OneToOneField(Userprofile, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.user.email
