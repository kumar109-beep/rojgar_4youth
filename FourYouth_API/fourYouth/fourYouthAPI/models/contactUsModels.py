from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import EmailField

class ContactUs(models.Model):
    name = models.CharField(max_length=20, blank=True)
    email = models.EmailField(max_length = 254)
    subject = models.CharField(max_length=20, blank=True)
    remarks = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email

