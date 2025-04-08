from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    avatar = models.ImageField(upload_to='avatars/', default='avatars/default.png')
    birth_date = models.DateField(null=True, blank=True)

    objects = models.Manager()

    def __str__(self):
        return f"{self.user.username} Profile"


