from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model


# Create your models here.
class Post(models.Model):
    heading = models.CharField(max_length=124, null=False, blank=False)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey('CustomUser', on_delete=models.CASCADE)

    def __str__(self):
        return self.heading

    def get_absolute_url(self):
        return reverse("posts")


class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)


class Comment(models.Model):
    author = models.ForeignKey("CustomUser", on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    comment = models.CharField(max_length=200)

    def __str__(self):
        return self.comment

    def get_absolute_url(self):
        return reverse("posts")