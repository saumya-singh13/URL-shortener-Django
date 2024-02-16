
from django.db import models


class ShortenedURL(models.Model):
    objects = None
    long_url = models.URLField()
    short_url = models.CharField(max_length=100)
