from django.db import models
from django.contrib.auth.models import User

class AboutUs(models.Model):
    bannerTitle = models.CharField(max_length=20, blank=True)
    descriptions = models.CharField(max_length=20, blank=True)
    bannerImages = models.FileField(upload_to="Upload_Images/adminSignature/", null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.bannerTitle