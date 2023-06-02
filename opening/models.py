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

    def __str__(self):
        return self.headline
