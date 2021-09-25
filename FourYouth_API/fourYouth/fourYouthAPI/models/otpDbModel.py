from django.db import models
from .userProfileModels import *

class OtpDbModel(models.Model):
    mobNO = models.CharField(max_length=11, blank=True)
    otpCode = models.CharField(max_length=6, blank=True)
    otpStatus = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # def __str__(self):
    #     return  self.userInstance.user.username
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["mobNO","otpCode"], name='OtpDbModel Constraints')
        ]