from django.contrib.auth.models import AbstractUser
from django.db import models
from home.managers.custom_user_manager import CustomUserManager

class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()
