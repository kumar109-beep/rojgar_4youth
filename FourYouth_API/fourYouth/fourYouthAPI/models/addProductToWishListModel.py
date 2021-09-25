from django.db import models
from django.contrib.auth.models import User
from .userProfileModels import *
from .productsListingModels import *

class AddToWishlist(models.Model):
    productfk = models.ForeignKey(ProductsListing, on_delete=models.CASCADE, null=True)
    userfk = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["productfk","userfk"], name='AddToWishlist Constraints')
        ]