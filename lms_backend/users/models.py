from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
# Create your models here.

USER_ROLES = (
    ('admin', 'Admin'),
    ('teacher', 'Teacher'),
    ('student', 'Student')
)

class User(AbstractUser):  # Abstract base class
    role = models.CharField(max_length=100, choices=USER_ROLES)
    mobile_no = models.CharField(max_length=12)