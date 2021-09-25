from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from rest_framework.decorators import api_view,permission_classes,authentication_classes,parser_classes
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from knox.auth import TokenAuthentication
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from django.contrib.auth.models import User

# Custome Import
from ..serializers.contactUsSerializers import *
from ..serializers.userProfileSerializers import *



@api_view(['GET'])
@parser_classes([MultiPartParser, FormParser, JSONParser])
# @permission_classes([IsAuthenticated])
def check_existing_data(request, format=None):
    str_data = request.query_params.get('q')
    type_of_search = request.query_params.get('type_of_search')
    if str_data != None and type_of_search == "username" and str_data != "":
        try:
            snippets = User.objects.get(username=str_data)
            return Response({'existing':True,"status":True,"message":"username already exist"})
        except User.DoesNotExist:
            return Response({'existing':False,"status":True,"message":"username avialable"})
            
    if str_data != None and type_of_search == "email" and str_data != "":
        try:
            snippets = User.objects.get(email=str_data)
            return Response({'existing':True,"status":True,"message":"email already exist"})
        except User.DoesNotExist:
            return Response({'existing':False,"status":True,"message":"email avialable"})

    if str_data != None and type_of_search == "contact" and str_data != "":
        try:
            snippets = UserProfile.objects.get(mobileNO=str_data)
            return Response({'existing':True,"status":True,"message":"contact already exist"})
        except UserProfile.DoesNotExist:
            return Response({'existing':False,"status":True,"message":"contact avialable"})
    else:
        return Response("Please Provide Correct key Parameter")

