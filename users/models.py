from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    email = models.EmailField(unique=True)
    first_name = models.CharField(blank=True, null=True, max_length=100, verbose_name="Имя")
    last_name = models.CharField(blank=True, null=True, max_length=100, verbose_name="Фамилия")


    def __str__(self):
        return self.username