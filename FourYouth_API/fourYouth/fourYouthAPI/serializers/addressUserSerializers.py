from rest_framework import serializers

# Custom Imports
from ..models.addressUserModel import *



class AddressListedBYUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddressListedBYUser
        fields = '__all__'

class GETAddressListedBYUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddressListedBYUser
        fields = '__all__'
        depth = 1

