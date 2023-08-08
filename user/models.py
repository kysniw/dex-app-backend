from django.db import models
from .managers import UserManager

# Create your models here.
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin
)


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    company_name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=6)
    street = models.CharField(max_length=255)
    first_login = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'

