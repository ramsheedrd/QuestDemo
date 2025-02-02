from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class ProfileImage(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile')
    created_at = models.DateTimeField(auto_now_add=True)
