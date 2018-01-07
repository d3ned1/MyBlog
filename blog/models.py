from statistics import mode

from django.contrib.auth.models import User
from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    user = models.ForeignKey(
        User,
        models.SET_NULL,
        blank=True,
        null=True,
    )
    def __str__(self):
        return self.title
