from django.contrib.auth.models import User
from django.db import models

class List(models.Model):
    name = models.TextField(max_length=255)
    description = models.TextField()
    public = models.BooleanField(default=False)
    slug = models.SlugField(unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,
        blank=True, null=True)

    def __str__(self):
        return self.name

class Item(models.Model):
    name = models.TextField(max_length=1000)
    done = models.BooleanField(default=False)
    list = models.ForeignKey(List, related_name='item', on_delete=models.CASCADE, #could be a problem?
        blank=True, null=True)

    def __str__(self):
        return self.name