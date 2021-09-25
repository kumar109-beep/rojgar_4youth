from rest_framework import serializers

# Custom Imports
from ..models.aboutUsModels import *



class AboutsUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUs
        fields = '__all__'

class GETAboutsUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUs
        fields = '__all__'
        depth = 1

