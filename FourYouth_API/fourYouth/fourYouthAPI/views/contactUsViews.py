from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from rest_framework.decorators import api_view,permission_classes,authentication_classes,parser_classes
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from knox.auth import TokenAuthentication
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination

# Custome Import
from ..serializers.contactUsSerializers import *


@api_view(['GET', 'POST'])
@parser_classes([MultiPartParser, FormParser, JSONParser])
@permission_classes([IsAuthenticated])
def contactUs_list(request, format=None):
    if request.method == 'POST':
        serializer = ContactUsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'data':serializer.data,'status':True,'message':"success"}, status=status.HTTP_201_CREATED)
        return Response({'data':serializer.errors,'status':True,'message':"fail"}, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        paginator = PageNumberPagination()
        snippets = ContactUs.objects.all().order_by('-created_at')
        snippets = paginator.paginate_queryset(snippets, request)
        serializer = GETContactUsSerializer(snippets, many=True)
        return Response({'data':serializer.data,'status':True,'message':"success"})


@api_view(['GET', 'POST'])
@parser_classes([MultiPartParser, FormParser, JSONParser])
# @permission_classes([IsAuthenticated])
def contactUs_list_web(request, format=None):
    if request.method == 'POST':
        serializer = ContactUsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'data':serializer.data,'status':True,'message':"success"}, status=status.HTTP_201_CREATED)
        return Response({'data':serializer.errors,'status':True,'message':"fail"}, status=status.HTTP_400_BAD_REQUEST)
   


@api_view(['GET','PUT','DELETE'])
@parser_classes([MultiPartParser, FormParser, JSONParser])
@permission_classes([IsAuthenticated])
def contactUs_detail(request, pk, format=None):
    try:
        contact_detail = ContactUs.objects.get(pk=pk)
    except ContactUs.DoesNotExist:
        return Response({'message': 'Batch Not Found! '},status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = GETContactUsSerializer(contact_detail)
        print(serializer.data)
        return JsonResponse({'data':serializer.data,'status':True,'message':"success"}, status=200, safe=False)

    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ContactUsSerializer(contact_detail, data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return JsonResponse({'data':serializer.data,'status':True,'message':"success"},)
        return JsonResponse({'data':serializer.errors,'status':True,'message':"fail"}, status=400)

    elif request.method == 'DELETE':
        contact_detail.delete()
        return Response({'data':{},'status':True,'message':"success"},status=status.HTTP_204_NO_CONTENT)



