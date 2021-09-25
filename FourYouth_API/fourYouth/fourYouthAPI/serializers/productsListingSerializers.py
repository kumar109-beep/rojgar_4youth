from rest_framework import serializers

# Custom Imports
from ..models.productsListingModels import *



class ProductsListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductsListing
        fields = '__all__'

class GETProductsListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductsListing
        fields = '__all__'
        depth = 1




class ProductsCategoryListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductsCategory
        fields = '__all__'

class GETProductsCategoryListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductsCategory
        fields = '__all__'
        depth = 1


