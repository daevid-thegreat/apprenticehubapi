from django.db import models
from opening.models import Opening
from authent.models import Userprofile


education_choices = (
    ('High School', 'High School'),
    ('Diploma', 'Diploma'),
    ('Bachelor', 'Bachelor'),
    ('Master', 'Master'),
    ('PhD', 'PhD')
)

age_choices = (
    ('18-25', '18-25'),
    ('26-35', '26-35'),
    ('36-45', '36-45'),
)

status_choices = (
    ('Pending', 'Pending'),
    ('Accepted', 'Accepted'),
    ('Rejected', 'Rejected')
)


# Create your models here.
class Application(models.Model):
    applicant = models.ForeignKey(Userprofile, on_delete=models.CASCADE)
    education = models.CharField(max_length=100, choices=education_choices)
    age = models.CharField(max_length=100, choices=age_choices)
    phone_number = models.CharField(max_length=20)
    message = models.TextField()
    opening = models.ForeignKey(Opening, on_delete=models.CASCADE)

    is_active = models.BooleanField(default=True)
    status = models.CharField(max_length=100, choices=status_choices, default='Pending')

    class Meta:
        verbose_name = ("application")
        verbose_name_plural = ("applications")

    def __str__(self):
        return f"{self.applicant} applied for {self.opening}"