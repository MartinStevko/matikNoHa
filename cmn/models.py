from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.PROTECT, default=1)
    obsah = models.TextField()
    cas = models.DateTimeField(default=timezone.now)
    schvalene = models.BooleanField(default=False)

    def __str__(self):
        return "Post {}".format(self.id)

class Backup(models.Model):
    author = models.ForeignKey(User, on_delete=models.PROTECT, default=1)
    obsah = models.TextField()
    cas = models.DateTimeField(default=timezone.now)
    schvalene = models.BooleanField(default=False)

    def __str__(self):
        return "Post {}".format(self.id)
