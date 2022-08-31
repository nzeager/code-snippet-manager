from django.contrib.auth.models import AbstractUser as BaseUser
from django.db import models

# Create your models here.


class User(BaseUser):
    # could add custom user attributes here
    pass


class Snippet(models.Model):
    title = models.CharField(max_length=255, default='')
    description = models.CharField(max_length=512, default='', blank=True)
    code = models.TextField()
    language = models.ForeignKey(
        'Language', on_delete=models.CASCADE, related_name='snippets', blank=True, null=True)
    # related name should be the plural of the model that it's in. This is a O2M relationship. A snippet has one user. A user can have many snippets.
    # user = models.ForeignKey(
    #     User, on_delete=models.CASCADE, related_name='snippets')
    # if I want to have more than one user associated with a snipped, I use a M2M field
    user = models.ManyToManyField(
        'User', related_name='snippets')
    author = models.ForeignKey(
        'User', on_delete=models.CASCADE, related_name='my_snippet')
    parent = models.ForeignKey(
        'Snippet', on_delete=models.SET_NULL, related_name='forks', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    tag = models.ManyToManyField('Tag', related_name='snippets', blank=True)

    def __str__(self):
        return f'{self.title} in {self.language}'


class Language(models.Model):
    name = models.CharField(max_length=255)
    version = models.FloatField(blank=True, null=True)

    def __str__(self):
        return f'{self.name} version {self.version}'


class Tag(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return f'{self.name}'
