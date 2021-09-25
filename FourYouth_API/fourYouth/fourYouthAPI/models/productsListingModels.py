from django.db import models
from django.contrib.auth.models import User



class ProductsCategory(models.Model):
    productCategoryName = models.CharField(max_length=50, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return  self.productCategoryName
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['productCategoryName'], name='ProductsCategory Listing')
        ]


class ProductsListing(models.Model):
    productName = models.CharField(max_length=50, blank=True)
    productCategory = models.ForeignKey(ProductsCategory,blank=True, on_delete=models.PROTECT)
    productCoverImages = models.FileField(upload_to="Upload_Images/productImages/", null=True,blank=True)
    productImages_one = models.FileField(upload_to="Upload_Images/productImages/", null=True,blank=True)
    productImages_two = models.FileField(upload_to="Upload_Images/productImages/", null=True,blank=True)
    productImages_three = models.FileField(upload_to="Upload_Images/productImages/", null=True,blank=True)
    productImages_four = models.FileField(upload_to="Upload_Images/productImages/", null=True,blank=True)
    productImages_five = models.FileField(upload_to="Upload_Images/productImages/", null=True,blank=True)
    productImages_six = models.FileField(upload_to="Upload_Images/productImages/", null=True,blank=True)
    productImages_sevenr = models.FileField(upload_to="Upload_Images/productImages/", null=True,blank=True)
    productDescription = models.TextField(blank=True)
    productDimension = models.CharField(max_length=50, blank=True)
    productPrice = models.IntegerField(blank=True)
    productQuantity = models.CharField(max_length=10, blank=True)
    productDisplay = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return  self.productName
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['productName'], name='Product Listing')
        ]