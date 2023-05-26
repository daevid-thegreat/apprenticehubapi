from django.db import models
from django.contrib.postgres.fields import ArrayField
from authent.models import Company


# Create your models here.
class Opening(models.Model):
    headline = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    pay = models.CharField(max_length=50)
    level = models.CharField(max_length=50)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    job_type = models.CharField(max_length=50)
    requirements = ArrayField(models.CharField(max_length=250), blank=True, null=True)

    def __str__(self):
        return self.headline
