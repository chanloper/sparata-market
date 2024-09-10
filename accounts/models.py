
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator
from django.utils import timezone


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    nickname = models.CharField(max_length=30, unique=True)
    birthday = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=10, choices=[
                              ('M', 'Male'), ('F', 'Female')], blank=True)
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.username
