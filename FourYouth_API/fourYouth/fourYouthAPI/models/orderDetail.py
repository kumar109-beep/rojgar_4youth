from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import EmailField
from .productsListingModels import *
from .addressUserModel import *

class OrderDetail(models.Model):
    orderID = models.CharField(max_length=20, blank=True)
    addressfk = models.ForeignKey(AddressListedBYUser,blank=True, null=True,on_delete=models.PROTECT)
    userfk = models.ForeignKey(User,blank=True, null=True,on_delete=models.PROTECT)
    productInfoM2M = models.ManyToManyField(ProductsListing)
    pay_status = models.CharField(max_length=20, blank=True)
    pay_type = models.CharField(max_length=20, blank=True)
    remarks = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.orderID

