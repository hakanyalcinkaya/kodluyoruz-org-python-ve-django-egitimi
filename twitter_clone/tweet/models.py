from django.db import models
from django.contrib.auth.models import User


class TweetPost(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE
    )
    post = models.CharField(max_length=240)
    like = models.PositiveIntegerField(default=0)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

