from django.contrib.auth.models import User
from django.db import models

class List(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    slug = models.SlugField(unique=True)
    # the new line we're adding
    user = models.ForeignKey(User, on_delete=models.CASCADE,
        blank=True, null=True)

    def __str__(self):
        return self.name

class Item(models.Model):
    name = models.CharField(max_length=255)

    list = models.ForeignKey(List, related_name='includeditems', on_delete=models.CASCADE,
        blank=True, null=True)

    def __str__(self):
        return self.name