from django.contrib.auth.models import AbstractUser as BaseUser
from django.db import models

# Create your models here.


class User(BaseUser):
    # could add custom user attributes here
    pass


class Snippet(models.Model):
    title = models.CharField(max_length=200)
    code = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title}'
