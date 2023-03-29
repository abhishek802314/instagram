from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

class User(AbstractUser):
    username = models.CharField(max_length=255, unique=True)
    first_name = models.CharField(max_length=55)
    last_name = models.CharField(max_length=55)
    last_action = models.DateTimeField(default=timezone.now, blank=True, null=True)
    is_online = models.BooleanField(default=False, blank=True, null=True)
    is_private = models.BooleanField(default=False)
    hide_status = models.BooleanField(default=False)


    def __str__(self):
        return self.username
    
    class Meta:
        ordering = ["id"]


class UserImage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField()

    def __str__(self):
        return self.user.username
    