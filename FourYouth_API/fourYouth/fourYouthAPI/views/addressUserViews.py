from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from rest_framework.decorators import api_view,permission_classes,authentication_classes,parser_classes
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from knox.auth import TokenAuthentication
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from django.db import IntegrityError

# Custome Import
from ..serializers.addressUserSerializers import *


@api_view(['GET', 'POST'])
@parser_classes([MultiPartParser, FormParser, JSONParser])
@permission_classes([IsAuthenticated])
def address_list(request, format=None):
    if request.method == 'POST':
        serializer = AddressListedBYUserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            try:
                serializer.save()
                return Response({'data':serializer.data,'status':True,'message':"success"}, status=status.HTTP_201_CREATED)
            except IntegrityError as e:
                return Response({'data':{},'status':False,'message':"Rows Alreday Exist"}, status=404)
        return Response({'data':serializer.errors,'status':True,'message':"fail"}, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        paginator = PageNumberPagination()
        snippets = AddressListedBYUser.objects.all().order_by('-updated_at')
        snippets = paginator.paginate_queryset(snippets, request)
        serializer = GETAddressListedBYUserSerializer(snippets, many=True)
        return Response({'data':serializer.data,'status':True,'message':"success"})

@api_view(['GET','PUT','DELETE'])
@parser_classes([MultiPartParser, FormParser, JSONParser])
@permission_classes([IsAuthenticated])
def address_detail(request, pk, format=None):
    try:
        contact_detail = AddressListedBYUser.objects.get(pk=pk)
    except AddressListedBYUser.DoesNotExist:
        return Response({'message': 'Batch Not Found! '},status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = GETAddressListedBYUserSerializer(contact_detail)
        print(serializer.data)
        return JsonResponse({'data':serializer.data,'status':True,'message':"success"}, status=200, safe=False)

    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = AddressListedBYUserSerializer(contact_detail, data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return JsonResponse({'data':serializer.data,'status':True,'message':"success"},)
        return JsonResponse({'data':serializer.errors,'status':True,'message':"fail"}, status=400)

    elif request.method == 'DELETE':
        contact_detail.delete()
        return Response({'data':{},'status':True,'message':"Deleted"},status=status.HTTP_204_NO_CONTENT)




@api_view(['GET','PUT','DELETE'])
@parser_classes([MultiPartParser, FormParser, JSONParser])
@permission_classes([IsAuthenticated])
def getAllAddressByUser(request, pk, format=None):
    if request.method == 'GET':
        contact_detail = AddressListedBYUser.objects.filter(userInstance__id=pk)
        serializer = GETAddressListedBYUserSerializer(contact_detail, many=True)
        return JsonResponse({'data':serializer.data,'status':True,'message':"success"}, status=200, safe=False)



