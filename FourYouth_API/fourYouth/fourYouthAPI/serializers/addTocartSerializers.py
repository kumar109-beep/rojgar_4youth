from rest_framework import serializers

# Custom Imports
from ..models.addTocartModels import *



class AddToCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddToCart
        fields = '__all__'

class GETAddToCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddToCart
        fields = '__all__'
        depth = 1
