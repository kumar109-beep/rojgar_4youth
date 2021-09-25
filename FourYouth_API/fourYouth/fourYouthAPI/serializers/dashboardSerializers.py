from rest_framework import serializers

# Custom Imports
from ..models.dashboardModels import *



class DashboardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dashboard
        fields = '__all__'

class GETDashboardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dashboard
        fields = '__all__'
        depth = 1

