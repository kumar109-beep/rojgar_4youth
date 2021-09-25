from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from rest_framework.decorators import api_view,permission_classes,authentication_classes,parser_classes
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from knox.auth import TokenAuthentication
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination

# Custome Import
from ..serializers.userProfileSerializers import *


@api_view(['GET', 'POST'])
@parser_classes([MultiPartParser, FormParser, JSONParser])
@permission_classes([IsAuthenticated])
def userProfile_list(request, format=None):
    if request.method == 'POST':
        serializer = UserProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({'data':serializer.errors,'status':True,'message':"fail"}, status=400)
    elif request.method == 'GET':
        paginator = PageNumberPagination()
        snippets = UserProfile.objects.all().order_by('-created_at')
        snippets = paginator.paginate_queryset(snippets, request)
        serializer = GETUserProfileSerializer(snippets, many=True)
        return Response(serializer.data)


@api_view(['GET','PUT','DELETE'])
@parser_classes([MultiPartParser, FormParser, JSONParser])
@permission_classes([IsAuthenticated])
def userProfile_detail(request, pk, format=None):
    try:
        product_detail = UserProfile.objects.get(pk=pk)
    except UserProfile.DoesNotExist:
        return Response({'message': 'Batch Not Found! '},status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = GETUserProfileSerializer(product_detail)
        print(serializer.data)
        return JsonResponse({'data':serializer.data,'status':True,'message':"success"},  status=200, safe=False)

    if request.method == 'PUT':
        data = JSONParser().parse(request)
        print(data)
        serializer = UserProfileSerializer(product_detail, data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return JsonResponse({'data':serializer.data,'status':True,'message':"success"}, status=201)
        return JsonResponse({'data':serializer.errors,'status':True,'message':"success"}, status=400)

    elif request.method == 'DELETE':
        try:
            product_detail.delete()
            return Response({'data':{},'status':True,'message':"Product Type Deleted"},status=200)
        except:
            return Response({'data':{},'status':False,'message':"Product Type Attched with Someone"},status=403)


