from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from rest_framework.decorators import api_view,permission_classes,authentication_classes,parser_classes
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from knox.auth import TokenAuthentication
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination

# Custome Import
from ..serializers.orderDeatilSerializers import *


@api_view(['GET', 'POST'])
@parser_classes([MultiPartParser, FormParser, JSONParser])
@permission_classes([IsAuthenticated])
def OrderDetail_list(request, format=None):
    if request.method == 'POST':
        serializer = OrderDetailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'data':serializer.data,'status':True,'message':"success"}, status=status.HTTP_201_CREATED)
        return Response({'data':serializer.errors,'status':True,'message':"fail"}, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        paginator = PageNumberPagination()
        snippets = OrderDetail.objects.all()
        snippets = paginator.paginate_queryset(snippets, request)
        serializer = GETOrderDetailSerializer(snippets, many=True)
        return Response({'data':serializer.data,'status':True,'message':"success"}, status=200)


@api_view(['GET','PUT','DELETE'])
@parser_classes([MultiPartParser, FormParser, JSONParser])
@permission_classes([IsAuthenticated])
def OrderDetail_detail(request, pk, format=None):
    try:
        about_detail = OrderDetail.objects.get(pk=pk)
    except OrderDetail.DoesNotExist:
        return Response({'message': 'Order Not Found! '},status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = GETOrderDetailSerializer(about_detail)
        print(serializer.data)
        return JsonResponse({'data':serializer.data,'status':True,'message':"success"}, status=200, safe=False)

    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = OrderDetailSerializer(about_detail, data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse({'data':serializer.errors,'status':True,'message':"fail"}, status=400)

    elif request.method == 'DELETE':
        about_detail.delete()
        return Response({'data':{},'status':True,'message':"success"},status=204)



