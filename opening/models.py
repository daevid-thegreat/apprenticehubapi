from django.db import models
from django.contrib.postgres.fields import ArrayField
from authent.models import Company

experience_level = (
    ('Entry Level', 'Entry Level'),
    ('Mid Level', 'Mid Level'),
    ('Senior Level', 'Senior Level'),
)
type = (
    ('Full Time', 'Full Time'),
    ('Part Time', 'Part Time'),
    ('Contract', 'Contract'),
    ('Internship', 'Internship'),
    ('Temporary', 'Temporary'),
)

industry_choices = (
    ('Accounting', 'Accounting'),
    ('Airlines/Aviation', 'Airlines/Aviation'),
    ('Alternative Dispute Resolution', 'Alternative Dispute Resolution'),
)


# Create your models here.
class Opening(models.Model):
    headline = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    pay = models.CharField(max_length=50)
    level = models.CharField(max_length=50, choices=experience_level)
    location = models.CharField(max_length=50)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    job_type = models.CharField(max_length=50, choices=type)
    industry = models.CharField(max_length=50, choices=industry_choices)
    requirements = ArrayField(models.CharField(max_length=250), blank=True, null=True)

    def __str__(self):
        return self.headline
