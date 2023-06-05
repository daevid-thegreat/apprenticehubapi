from django.db import models
from django.contrib.postgres.fields import ArrayField
from authent.models import Company
from uuid import uuid4


# Create your models here.
class Opening(models.Model):

    uid = models.UUIDField(default=uuid4, editable=False, unique=True)
    headline = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
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

    def __str__(self):
        return self.opening.headline
