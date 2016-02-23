from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User, Group


class Joke(models.Model):
    date_add = models.DateTimeField(auto_now_add=True)
    text = models.TextField(verbose_name="Joke")
    funny = models.BooleanField(default=False)
    user = models.ForeignKey(User)


class VoteUp(models.Model):
    date_add = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User)
    joke = models.ForeignKey(Joke)

    class Meta:
        unique_together = ('user', 'joke')


class ExtendedGroupDescriptionForExampleHowToUseRestApi(Group):
    description = models.TextField()