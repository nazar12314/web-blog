from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractBaseUser


# Create your models here.
class Post(models.Model):
    heading = models.CharField(max_length=124, null=False, blank=False)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.heading

    def get_absolute_url(self):
        return reverse("posts")


class CustomUser(AbstractBaseUser):
    
    email = models.EmailField(verbose_name="email address", unique=True, max_length=124)
    is_active = models.BooleanField(default=False)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)

    REQUIRED_FIELDS = ['email']