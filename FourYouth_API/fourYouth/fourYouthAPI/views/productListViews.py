from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from rest_framework.decorators import api_view,permission_classes,authentication_classes,parser_classes
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from knox.auth import TokenAuthentication
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from django.db.models import Q

# Custome Import
from ..serializers.productsListingSerializers import *


@api_view(['GET', 'POST'])
@parser_classes([MultiPartParser, FormParser, JSONParser])
@permission_classes([IsAuthenticated])
def product_list(request, format=None):
    if request.method == 'POST':
        serializer = ProductsListingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({'data':serializer.errors,'status':True,'message':"fail"}, status=400)
    elif request.method == 'GET':
        paginator = PageNumberPagination()
        snippets = ProductsListing.objects.all().order_by('-created_at')
        snippets = paginator.paginate_queryset(snippets, request)
        serializer = GETProductsListingSerializer(snippets, many=True)
        return Response(serializer.data)


@api_view(['GET','PUT','DELETE'])
@parser_classes([MultiPartParser, FormParser, JSONParser])
@permission_classes([IsAuthenticated])
def product_detail(request, pk, format=None):
    try:
        product_detail = ProductsListing.objects.get(pk=pk)
    except ProductsListing.DoesNotExist:
        return Response({'message': 'Batch Not Found! '},status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = GETProductsListingSerializer(product_detail)
        print(serializer.data)
        return JsonResponse({'data':serializer.data,'status':True,'message':"success"},  status=200, safe=False)

    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ProductsListingSerializer(product_detail, data=data)
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





@api_view(['GET', 'POST'])
@parser_classes([MultiPartParser, FormParser, JSONParser])
@permission_classes([IsAuthenticated])
def productCategory_list(request, format=None):
    if request.method == 'POST':
        serializer = ProductsCategoryListingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'data':serializer.data,'status':True,'message':"success"}, status=201)
        return Response({'data':serializer.errors,'status':True,'message':"success"}, status=400)
    elif request.method == 'GET':
        paginator = PageNumberPagination()
        snippets = ProductsCategory.objects.all().order_by('-created_at')
        snippets = paginator.paginate_queryset(snippets, request)
        serializer = GETProductsCategoryListingSerializer(snippets, many=True)
        return Response({'data':serializer.data,'status':True,'message':"success"}, status=200)


@api_view(['GET','PUT','DELETE'])
@parser_classes([MultiPartParser, FormParser, JSONParser])
@permission_classes([IsAuthenticated])
def productCategory_detail(request, pk, format=None):
    try:
        product_detail = ProductsCategory.objects.get(pk=pk)
    except ProductsCategory.DoesNotExist:
        return Response({'message': 'Batch Not Found! '},status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = GETProductsCategoryListingSerializer(product_detail)
        print(serializer.data)
        return JsonResponse(serializer.data, status=200, safe=False)

    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ProductsCategoryListingSerializer(product_detail, data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return JsonResponse({'data':serializer.data,'status':True,'message':"success"}, status=201)
        return JsonResponse({'data':serializer.errors,'status':True,'message':"success"}, status=400)

    elif request.method == 'DELETE':
        try:
            product_detail.delete()
            return Response({'data':{},'status':True,'message':"Category Type Deleted"},status=200)
        except:
            return Response({'data':{},'status':False,'message':"Category Type Attched with Someone"},status=403)



@api_view(['GET', 'POST'])
@parser_classes([MultiPartParser, FormParser, JSONParser])
# @permission_classes([IsAuthenticated])
def product_list_web(request, format=None):
    if request.method == 'GET':
        paginator = PageNumberPagination()
        snippets = ProductsListing.objects.all().order_by('-created_at')
        snippets = paginator.paginate_queryset(snippets, request)
        serializer = GETProductsListingSerializer(snippets, many=True)
        return Response({'data':serializer.data,'status':True,'message':"success"},  status=200)


@api_view(['GET','PUT','DELETE'])
@parser_classes([MultiPartParser, FormParser, JSONParser])
# @permission_classes([IsAuthenticated])
def product_detail_web(request, pk, format=None):
    try:
        product_detail = ProductsListing.objects.get(pk=pk)
    except ProductsListing.DoesNotExist:
        return Response({'message': 'Product  Not Found! '},status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = GETProductsListingSerializer(product_detail)
        print(serializer.data)
        return JsonResponse({'data':serializer.data,'status':True,'message':"success"},  status=200, safe=False)




@api_view(['GET','PUT','DELETE'])
@parser_classes([MultiPartParser, FormParser, JSONParser])
# @permission_classes([IsAuthenticated])
def product_detail_related_web(request, pk, format=None):
    if request.method == 'GET':
        product_detail = ProductsListing.objects.filter(productCategory__id=pk)[:3]
        print(product_detail)
        serializer = GETProductsListingSerializer(product_detail, many=True)
        return JsonResponse({'data':serializer.data,'status':True,'message':"success"},  status=200, safe=False)

@api_view(['GET','PUT','DELETE'])
@permission_classes([IsAuthenticated])
@parser_classes([MultiPartParser, FormParser, JSONParser])
@permission_classes([IsAuthenticated])
def product_display_status(request, pk, format=None):
    try:
        product_detail = ProductsListing.objects.get(pk=pk)
    except ProductsListing.DoesNotExist:
        return Response({'message': 'Batch Not Found! '},status=status.HTTP_404_NOT_FOUND)
    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ProductsListingSerializer(product_detail, data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return JsonResponse({'data':serializer.data,'status':True,'message':"success"}, status=201)
        return JsonResponse({'data':serializer.errors,'status':True,'message':"success"}, status=400)




@api_view(['GET', 'POST'])
@parser_classes([MultiPartParser, FormParser, JSONParser])
# @permission_classes([IsAuthenticated])
def productCategory_list_web(request, format=None):
    if request.method == 'GET':
        paginator = PageNumberPagination()
        snippets = ProductsCategory.objects.all().order_by('-created_at')
        snippets = paginator.paginate_queryset(snippets, request)
        serializer = GETProductsCategoryListingSerializer(snippets, many=True)
        return Response({'data':serializer.data,'status':True,'message':"success"},  status=200)


@api_view(['GET', 'POST'])
@parser_classes([MultiPartParser, FormParser, JSONParser])
def filterproduct_web(request, format=None):
    if request.method == 'GET':
        if request.query_params.get('filterKey') == "category_filter":
            dataList = eval(request.query_params.get('category_filter_data'))
            # print(type(dataList))
            productData = ProductsListing.objects.filter(productCategory__id__in=dataList)
            serializer = ProductsListingSerializer(productData, many=True)
            return Response({'data':serializer.data,'status':True,'message':"success"},  status=200)
        elif request.query_params.get('filterKey') == "sortByPrice":
            if request.query_params.get('sortByPrice') == "hightToLow":
                productData = ProductsListing.objects.all().order_by('-productPrice')
                serializer = ProductsListingSerializer(productData, many=True)
                return Response({'data':serializer.data,'status':True,'message':"success"},  status=200)
            elif request.query_params.get('sortByPrice') == "lowToHigh":
                productData = ProductsListing.objects.all().order_by('productPrice')
                serializer = ProductsListingSerializer(productData, many=True)
                return Response({'data':serializer.data,'status':True,'message':"success"},  status=200)
            else:
                return Response({'data':"Please Provide Correct Params",'status':True,'message':"success"},  status=200)
        elif request.query_params.get('filterKey') == "priceRange":
            dataList = eval(request.query_params.get('sortByPriceRange'))
            productData = ProductsListing.objects.filter(productPrice__range=dataList)
            serializer = ProductsListingSerializer(productData, many=True)
            return Response({'data':serializer.data,'status':True,'message':"success"},  status=200)
        elif request.query_params.get('filterKey') == "serachBox":
            search_text = request.query_params.get('search_text')
            productData = ProductsListing.objects.filter(Q(productName__icontains=search_text))
            serializer = ProductsListingSerializer(productData, many=True)
            return Response({'data':serializer.data,'status':True,'message':"success"},  status=200)
        elif request.query_params.get('filterKey') == "categoryWithSortByPrice":
            dataList = eval(request.query_params.get('category_filter_data'))
            if request.query_params.get('sortByPrice') == "hightToLow":
                productData = ProductsListing.objects.filter(productCategory__id__in=dataList).order_by('-productPrice')
                serializer = ProductsListingSerializer(productData, many=True)
                return Response({'data':serializer.data,'status':True,'message':"success"},  status=200)
            elif request.query_params.get('sortByPrice') == "lowToHigh":
                productData = ProductsListing.objects.filter(productCategory__id__in=dataList).order_by('productPrice')
                serializer = ProductsListingSerializer(productData, many=True)
                return Response({'data':serializer.data,'status':True,'message':"success"},  status=200)
            else:
                return Response({'data':"Please Provide Correct Params",'status':True,'message':"success"},  status=200)
        elif request.query_params.get('filterKey') == "sortBypriceWithrange":
            dataList = eval(request.query_params.get('sortByPriceRange'))
            if request.query_params.get('sortByPrice') == "hightToLow":
                productData = ProductsListing.objects.filter(productPrice__range=dataList).order_by('-productPrice')
                serializer = ProductsListingSerializer(productData, many=True)
                return Response({'data':serializer.data,'status':True,'message':"success"},  status=200)
            elif request.query_params.get('sortByPrice') == "lowToHigh":
                productData = ProductsListing.objects.filter(productPrice__range=dataList).order_by('productPrice')
                serializer = ProductsListingSerializer(productData, many=True)
                return Response({'data':serializer.data,'status':True,'message':"success"},  status=200)
            else:
                return Response({'data':"Please Provide Correct Params",'status':True,'message':"success"},  status=200)
        elif request.query_params.get('filterKey') == "categoryWithPriceRange":
            dataList = eval(request.query_params.get('category_filter_data'))
            dataListrnage = eval(request.query_params.get('sortByPriceRange'))
            productData = ProductsListing.objects.filter(productCategory__id__in=dataList,productPrice__range=dataListrnage)
            serializer = ProductsListingSerializer(productData, many=True)
            return Response({'data':serializer.data,'status':True,'message':"success"},  status=200)
        elif request.query_params.get('filterKey') == "sideFilterAll":
            dataList = eval(request.query_params.get('category_filter_data'))
            dataListrnage = eval(request.query_params.get('sortByPriceRange'))
            if request.query_params.get('sortByPrice') == "hightToLow":
                productData = ProductsListing.objects.filter(productCategory__id__in=dataList,productPrice__range=dataListrnage).order_by('-productPrice')
                serializer = ProductsListingSerializer(productData, many=True)
                return Response({'data':serializer.data,'status':True,'message':"success"},  status=200)
            elif request.query_params.get('sortByPrice') == "lowToHigh":
                productData = ProductsListing.objects.filter(productCategory__id__in=dataList,productPrice__range=dataListrnage).order_by('productPrice')
                serializer = ProductsListingSerializer(productData, many=True)
                return Response({'data':serializer.data,'status':True,'message':"success"},  status=200)
            else:
                return Response({'data':"Please Provide Correct Params",'status':True,'message':"success"},  status=200)
        # Search Box

        elif request.query_params.get('filterKey') == "categoryWithsearchBox":
            dataList = eval(request.query_params.get('category_filter_data'))
            search_text = request.query_params.get('search_text')
            productData = ProductsListing.objects.filter(productCategory__id__in=dataList)
            productData = productData.filter(Q(productName__icontains=search_text))
            serializer = ProductsListingSerializer(productData, many=True)
            return Response({'data':serializer.data,'status':True,'message':"success"},  status=200)


        elif request.query_params.get('filterKey') == "sortByPriceWithSearchBox":
            search_text = request.query_params.get('search_text')
            if request.query_params.get('sortByPrice') == "hightToLow":
                productData = ProductsListing.objects.filter(Q(productName__icontains=search_text)).order_by('-productPrice')
                serializer = ProductsListingSerializer(productData, many=True)
                return Response({'data':serializer.data,'status':True,'message':"success"},  status=200)
            elif request.query_params.get('sortByPrice') == "lowToHigh":
                productData = ProductsListing.objects.filter(Q(productName__icontains=search_text)).order_by('productPrice')
                serializer = ProductsListingSerializer(productData, many=True)
                return Response({'data':serializer.data,'status':True,'message':"success"},  status=200)
            else:
                return Response({'data':"Please Provide Correct Params",'status':True,'message':"success"},  status=200)

   

        elif request.query_params.get('filterKey') == "sortByPriceRangeWithSearchBox":
            search_text = request.query_params.get('search_text')
            dataListrnage = eval(request.query_params.get('sortByPriceRange'))
            productData = ProductsListing.objects.filter(productPrice__range=dataListrnage)
            productData = productData.filter(Q(productName__icontains=search_text)).order_by('-productPrice')
            serializer = ProductsListingSerializer(productData, many=True)
            return Response({'data':serializer.data,'status':True,'message':"success"},  status=200)






        elif request.query_params.get('filterKey') == "categorySortPriceWithSearchBox":
            dataList = eval(request.query_params.get('category_filter_data'))
            search_text = request.query_params.get('search_text')
            if request.query_params.get('sortByPrice') == "hightToLow":
                productData = ProductsListing.objects.filter(productCategory__id__in=dataList)
                productData = productData.filter(Q(productName__icontains=search_text)).order_by('-productPrice')
                serializer = ProductsListingSerializer(productData, many=True)
                return Response({'data':serializer.data,'status':True,'message':"success"},  status=200)
            elif request.query_params.get('sortByPrice') == "lowToHigh":
                productData = ProductsListing.objects.filter(productCategory__id__in=dataList)
                productData = productData.filter(Q(productName__icontains=search_text)).order_by('productPrice')
                serializer = ProductsListingSerializer(productData, many=True)
                return Response({'data':serializer.data,'status':True,'message':"success"},  status=200)
            else:
                return Response({'data':"Please Provide Correct Params",'status':True,'message':"success"},  status=200)



        elif request.query_params.get('filterKey') == "SortPriceByRangeWithSearchBox":
            dataList = eval(request.query_params.get('sortByPriceRange'))
            search_text = request.query_params.get('search_text')
            if request.query_params.get('sortByPrice') == "hightToLow":
                productData = ProductsListing.objects.filter(productPrice__range=dataList)
                productData = productData.filter(Q(productName__icontains=search_text)).order_by('-productPrice')
                serializer = ProductsListingSerializer(productData, many=True)
                return Response({'data':serializer.data,'status':True,'message':"success"},  status=200)
            elif request.query_params.get('sortByPrice') == "lowToHigh":
                productData = ProductsListing.objects.filter(productPrice__range=dataList)
                productData = productData.filter(Q(productName__icontains=search_text)).order_by('productPrice')
                serializer = ProductsListingSerializer(productData, many=True)
                return Response({'data':serializer.data,'status':True,'message':"success"},  status=200)
            else:
                return Response({'data':"Please Provide Correct Params",'status':True,'message':"success"},  status=200)





        elif request.query_params.get('filterKey') == "categortyPriceRangeWithSearchBox":
            dataList = eval(request.query_params.get('category_filter_data'))
            dataListrnage = eval(request.query_params.get('sortByPriceRange'))
            search_text = request.query_params.get('search_text')
            productData = ProductsListing.objects.filter(productCategory__id__in=dataList,productPrice__range=dataListrnage)
            productData = productData.filter(Q(productName__icontains=search_text)).order_by('-productPrice')
            serializer = ProductsListingSerializer(productData, many=True)
            return Response({'data':serializer.data,'status':True,'message':"success"},  status=200)
       
        
        
        elif request.query_params.get('filterKey') == "FilterAll":
            dataList = eval(request.query_params.get('category_filter_data'))
            dataListrnage = eval(request.query_params.get('sortByPriceRange'))
            search_text = request.query_params.get('search_text')
            if request.query_params.get('sortByPrice') == "hightToLow":
                productData = ProductsListing.objects.filter(productCategory__id__in=dataList,productPrice__range=dataListrnage)
                productData = productData.filter(Q(productName__icontains=search_text)).order_by('-productPrice')
                serializer = ProductsListingSerializer(productData, many=True)
                return Response({'data':serializer.data,'status':True,'message':"success"},  status=200)
            elif request.query_params.get('sortByPrice') == "lowToHigh":
                productData = ProductsListing.objects.filter(productCategory__id__in=dataList,productPrice__range=dataListrnage)
                productData = productData.filter(Q(productName__icontains=search_text)).order_by('productPrice')
                serializer = ProductsListingSerializer(productData, many=True)
                return Response({'data':serializer.data,'status':True,'message':"success"},  status=200)
            else:
                return Response({'data':"Please Provide Correct Params",'status':True,'message':"success"},  status=200)

        else:
            return Response({'data':"Please Provide Correct Params",'status':True,'message':"success"},  status=200)

            
            