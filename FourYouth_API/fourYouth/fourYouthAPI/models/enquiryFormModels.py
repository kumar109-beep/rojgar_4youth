from django.db import models
from django.contrib.auth.models import User
from .productsListingModels import *
from .userProfileModels import *
from .addressUserModel import *





class EnquiryForm(models.Model):
    contactNo = models.CharField(max_length=10, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return  self.contactNo
   



class EnquiryFormData(models.Model):
    productfk = models.ForeignKey(ProductsListing, on_delete=models.PROTECT,null=True)
    enquiryfk = models.ForeignKey(EnquiryForm, on_delete=models.PROTECT,null=True)
    userfk = models.ForeignKey(UserProfile, on_delete=models.PROTECT,null=True)
    name = models.CharField(max_length=20, blank=True)
    email = models.EmailField(max_length = 254, null=True, blank=True)
    state = models.CharField(max_length=30, blank=True)
    city = models.CharField(max_length=30, blank=True)
    address = models.TextField(blank=True)
    remarks = models.TextField(blank=True)
    status = models.CharField(max_length=30, blank=True, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)