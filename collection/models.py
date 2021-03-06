from django.contrib.auth.models import User
from django.db import models

class List(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    public = models.BooleanField(default=False)
    slug = models.SlugField(unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,
        blank=True, null=True)

    def __str__(self):
        return self.name

class Item(models.Model):
    name = models.CharField(max_length=255)
    done = models.BooleanField(default=False)
    list = models.ForeignKey(List, related_name='includeditems', on_delete=models.CASCADE, #could be a problem?
        blank=True, null=True)

    def __str__(self):
        return self.name