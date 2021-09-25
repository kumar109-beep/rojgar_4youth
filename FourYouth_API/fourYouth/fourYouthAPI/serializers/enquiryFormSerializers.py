from rest_framework import serializers

# Custom Imports
from ..models.enquiryFormModels import *



class EnquiryFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = EnquiryForm
        fields = '__all__'

class GETEnquiryFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = EnquiryForm
        fields = '__all__'
        depth = 1

class EnquiryFormDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = EnquiryFormData
        fields = '__all__'

class GETEnquiryFormDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = EnquiryFormData
        fields = '__all__'
        depth = 1

