from django.db import models
from django.contrib.auth.models import AbstractUser


class UserModel(AbstractUser):
    phone = models.CharField(max_length=13)
    zip_code = models.PositiveIntegerField()
    address = models.CharField(max_length=255)
    card = models.CharField(max_length=16)

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
# Create your models here.
