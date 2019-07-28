from django.db import models
from django.contrib.auth.models import User


class PasswordToken(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE
    )
    token = models.CharField(max_length=16)
    activated = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)