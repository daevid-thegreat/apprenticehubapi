from django.db import models
from django.contrib.postgres.fields import ArrayField
from authent.models import Company
from uuid import uuid4


# Create your models here.
class Opening(models.Model):

    uid = models.UUIDField(default=uuid4, editable=False, unique=True)
    headline = models.CharField(max_length=50)
    description = models.CharField(max_length=400)
    pay = models.CharField(max_length=50)
    level = models.CharField(max_length=50)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    job_type = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    status = models.CharField(max_length=50, default='open')

    def __str__(self):
        return self.headline


class Application(models.Model):
    opening = models.ForeignKey(Opening, on_delete=models.CASCADE)
    user = models.ForeignKey('authent.Userprofile', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    email = models.CharField(max_length=50)
    education = models.CharField(max_length=50)
    age = models.CharField(max_length=50)
    tel = models.CharField(max_length=50)
    message = models.CharField(max_length=300)

    status = models.CharField(max_length=50, default='pending')

    def name(self):
        return self.user.name
    def __str__(self):
        return self.opening.headline


class Apprentice(models.Model):
    uid = models.UUIDField(default=uuid4, editable=False, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='apprentices')
    created_at = models.DateTimeField(auto_now_add=True)
    pay = models.CharField(max_length=50)

    def __str__(self):
        return self.first_name
