from django.db import models
from django.db.models.fields import CharField


class Mission(models.Model):
    username = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    confirm_password = models.CharField(max_length=200)
