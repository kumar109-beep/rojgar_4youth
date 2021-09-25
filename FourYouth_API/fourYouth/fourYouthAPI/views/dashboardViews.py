from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from rest_framework.decorators import api_view,permission_classes,authentication_classes,parser_classes
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from knox.auth import TokenAuthentication
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination

# Custome Import
from ..serializers.dashboardSerializers import *
from ..serializers.enquiryFormSerializers import *
from ..serializers.productsListingSerializers import *


@api_view(['GET', 'POST'])
@parser_classes([MultiPartParser, FormParser, JSONParser])
@permission_classes([IsAuthenticated])
def dashboard_list(request, format=None):
    if request.method == 'POST':
        serializer = DashboardSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'data':serializer.data,'status':True,'message':"success"}, status=201)
        return Response({'data':serializer.errors,'status':True,'message':"fail"}, status=400)
    elif request.method == 'GET':
        paginator = PageNumberPagination()
        snippets = Dashboard.objects.all()
        snippets = paginator.paginate_queryset(snippets, request)
        serializer = GETDashboardSerializer(snippets, many=True)
        return Response({'data':serializer.data,'status':True,'message':"success"}, status=200)


@api_view(['GET','PUT','DELETE'])
@parser_classes([MultiPartParser, FormParser, JSONParser])
@permission_classes([IsAuthenticated])
def dashboard_detail(request, pk, format=None):
    try:
        batchDetail = Dashboard.objects.get(pk=pk)
    except Dashboard.DoesNotExist:
        return Response({'data':{},'status':True,'message': 'Batch Not Found! '},status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = GETDashboardSerializer(batchDetail)
        print(serializer.data)
        return JsonResponse({'data':serializer.data,'status':True,'message':"success"}, status=200, safe=False)

    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = DashboardSerializer(batchDetail, data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return JsonResponse({'data':serializer.data,'status':True,'message':"success"}, status=200)
        return JsonResponse({'data':serializer.errors,'status':True,'message':"fail"}, status=400)

    elif request.method == 'DELETE':
        batchDetail.delete()
        return Response({'data':{"Deleted"},'status':True,'message':"success"}, status=204)



@api_view(['GET', 'POST'])
@parser_classes([MultiPartParser, FormParser, JSONParser])
# @permission_classes([IsAuthenticated])
def dashboard_count(request, format=None):
    if request.method == 'GET':
        paginator = PageNumberPagination()
        snippets1 = EnquiryForm.objects.all().count()
        snippets2 = EnquiryFormData.objects.all().count()
        snippets3 = EnquiryFormData.objects.filter(status='delivered').count()
        return Response({'tl_cust':snippets1,'tl_query':snippets2,'tl_com_query':snippets3,'status':True,'message':"success"}, status=200)


@api_view(['GET', 'POST'])
@parser_classes([MultiPartParser, FormParser, JSONParser])
# @permission_classes([IsAuthenticated])
def dashboard_product(request, format=None):
    if request.method == 'GET':
        paginator = PageNumberPagination()
        snippets = ProductsListing.objects.all().order_by('-created_at')[:5]
        snippets = paginator.paginate_queryset(snippets, request)
        serializer = GETProductsListingSerializer(snippets, many=True)
        return Response({'data':serializer.data,'status':True,'message':"success"}, status=200)



@api_view(['GET', 'POST'])
@parser_classes([MultiPartParser, FormParser, JSONParser])
# @permission_classes([IsAuthenticated])
def dashboard_enquiry(request, format=None):
    if request.method == 'GET':
        paginator = PageNumberPagination()
        snippets = EnquiryFormData.objects.all().order_by('-created_at')[:5]
        snippets = paginator.paginate_queryset(snippets, request)
        serializer = EnquiryFormDataSerializer(snippets, many=True)
        return Response({'data':serializer.data,'status':True,'message':"success"}, status=200)




@api_view(['GET', 'POST'])
@parser_classes([MultiPartParser, FormParser, JSONParser])
# @permission_classes([IsAuthenticated])
def dashboard_list_web(request, format=None):
    if request.method == 'GET':
        paginator = PageNumberPagination()
        snippets = Dashboard.objects.all()
        snippets = paginator.paginate_queryset(snippets, request)
        serializer = GETDashboardSerializer(snippets, many=True)
        return Response({'data':serializer.data,'status':True,'message':"success"}, status=200)

