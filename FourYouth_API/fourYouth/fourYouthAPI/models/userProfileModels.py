from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT,null=True,blank=True)
    mobileNO = models.CharField(max_length=12, blank=True)
    location = models.CharField(max_length=30, blank=True)
    address = models.TextField(max_length=500, blank=True)
    user_image = models.FileField(upload_to="Upload_Images/UserImages/", null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return  str(self.mobileNO)
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['mobileNO'], name='UserProfile Constraint')
        ]