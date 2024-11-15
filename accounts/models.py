from django.db import models
from django.contrib.auth.models import AbstractUser


class Customer(AbstractUser):
    phone = models.CharField(max_length=15, unique=True)
    email = models.EmailField(unique=True)
    