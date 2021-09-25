from django.db import models
from .userProfileModels import *

class AddressListedBYUser(models.Model):
    userInstance = models.ForeignKey(UserProfile,blank=True, on_delete=models.PROTECT)
    address = models.TextField(max_length=100,blank=True)
    fullname = models.CharField(max_length=100,blank=True)
    contact = models.CharField(max_length=100,blank=True)
    district = models.CharField(max_length=100,blank=True)
    landmark = models.CharField(max_length=50, blank=True)
    state = models.CharField(max_length=50, blank=True)
    pincode = models.CharField(max_length=6, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return  self.userInstance.user.username
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["address","landmark","state","pincode"], name='AddressListedBYUser Constraints')
        ]