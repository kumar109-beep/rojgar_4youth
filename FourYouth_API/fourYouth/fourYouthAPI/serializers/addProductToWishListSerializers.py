from rest_framework import serializers

# Custom Imports
from ..models.addProductToWishListModel import *



class AddProductToWishListSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddToWishlist
        fields = '__all__'

class GETAddProductToWishListSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddToWishlist
        fields = '__all__'
        depth = 1
