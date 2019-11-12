from django.contrib.auth.models import User
from django.db import models

class List(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    slug = models.SlugField(unique=True)
    # the new line we're adding
    user = models.OneToOneField(User, on_delete=models.CASCADE,
        blank=True, null=True)