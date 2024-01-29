from django.db import models
from django.contrib.auth.models import AbstractUser

# Define a custom user model that extends AbstractUser
class CustomUserModel(AbstractUser):
    # Available choices for class levels
    CLASS_LEVEL = [
        ('Year_one', 'Year One'),
        ('Year_two', 'Year Two'),
        ('Year_three', 'Year Three'),
        ('other', 'Other'),
    ]

    # Class level field with choices and default value
    class_level = models.CharField(
        max_length=50,
        choices=CLASS_LEVEL,
        default="Year_one",
    )

    # Name of the school field
    name_of_school = models.CharField(
        max_length=50,
    )

    # Email field
    email = models.EmailField(
        max_length=100,
    )

# Define a model for research data
class ResearchModel(models.Model):
    # Title of the research with a maximum length of 500 characters
    title = models.TextField(max_length=500, blank=False)

    # Description of the research with a maximum length of 5000 characters
    description = models.TextField(max_length=5000, blank=False)
