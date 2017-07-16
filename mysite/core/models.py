from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.CharField(max_length=50, blank=True)
    dob = models.DateField(default=timezone.now)
    year = models.CharField(max_length=4)
    mobile = models.CharField(max_length=10)
    enrollment_no = models.CharField(max_length=4)
