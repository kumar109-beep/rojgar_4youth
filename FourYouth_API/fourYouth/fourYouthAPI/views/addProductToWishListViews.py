from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from rest_framework.decorators import api_view,permission_classes,authentication_classes,parser_classes
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from knox.auth import TokenAuthentication
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from django.db import IntegrityError
from django.db.models import Q

# Custome Import
from ..serializers.addProductToWishListSerializers import *
from ..serializers.addTocartSerializers import *
from ..serializers.productsListingSerializers import *


@api_view(['GET', 'POST'])
@parser_classes([MultiPartParser, FormParser, JSONParser])
@permission_classes([IsAuthenticated])
def addToWishlist_list(request, format=None):
    if request.method == 'POST':
        serializer = AddProductToWishListSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            try:
                serializer.save()
                return Response({'data':serializer.data,'status':True,'message':"success"}, status=status.HTTP_201_CREATED)
            except IntegrityError as e:
                return Response({'data':{},'status':False,'message':"Rows Alreday Exist"}, status=404)
        return Response({'data':serializer.errors,'status':True,'message':"fail"}, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        paginator = PageNumberPagination()
        snippets = AddToWishlist.objects.all().order_by('-updated_at')
        snippets = paginator.paginate_queryset(snippets, request)
        serializer = GETAddProductToWishListSerializer(snippets, many=True)
        return Response({'data':serializer.data,'status':True,'message':"success"})

@api_view(['GET','PUT','DELETE'])
@parser_classes([MultiPartParser, FormParser, JSONParser])
@permission_classes([IsAuthenticated])
def addToWishlist_detail(request, pk, format=None):
    try:
        contact_detail = AddToWishlist.objects.filter(userfk__id=pk)
    except AddToWishlist.DoesNotExist:
        return Response({'message': 'No Item Found! '},status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = GETAddProductToWishListSerializer(contact_detail,many=True)
        print(serializer.data)
        return JsonResponse({'data':serializer.data,'status':True,'message':"success"}, status=200, safe=False)

    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = AddProductToWishListSerializer(contact_detail, data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return JsonResponse({'data':serializer.data,'status':True,'message':"success"},)
        return JsonResponse({'data':serializer.errors,'status':True,'message':"fail"}, status=400)

    elif request.method == 'DELETE':
        # contact_detail.delete()
        contact_detail = AddToWishlist.objects.filter(id=pk).delete()
        return Response({'data':{},'status':True,'message':"Deleted"},status=status.HTTP_204_NO_CONTENT)



@api_view(['GET', 'POST'])
@parser_classes([MultiPartParser, FormParser, JSONParser])
@permission_classes([IsAuthenticated])
def checkCurrentlyAddOrNotproduct(request, format=None):
    try:
        contact_detail = AddToWishlist.objects.get(userfk__id=request.data['userfk'],productfk__id=request.data['productfk'])
        return Response({'data':"Item Already Exist",'status':True,'message':"exist"},status=200)
    except AddToWishlist.DoesNotExist:
        return Response({'data':"Item Not Exist",'status':True,'message':"not exist"},status=status.HTTP_404_NOT_FOUND)



@api_view(['GET', 'POST'])
@parser_classes([MultiPartParser, FormParser, JSONParser])
@permission_classes([IsAuthenticated])
def CheckAdd_wishlist(request, format=None):
    if request.method == 'GET':
        if request.data['action'] == "remove":
            try:
                contact_detail = AddToWishlist.objects.get(userfk__id=request.data['userfk'],productfk__id=request.data['productfk'])
                contact_detail.delete()
                return Response({'data':"Item Successfully Remove",'status':True,'message':"Deleted"},status=status.HTTP_204_NO_CONTENT)
            except AddToWishlist.DoesNotExist:
                return Response({'message': 'No Item Found! '},status=status.HTTP_404_NOT_FOUND)
        else:
            serializer = AddProductToWishListSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                try:
                    serializer.save()
                    return Response({'data':serializer.data,'status':True,'message':"success"}, status=status.HTTP_201_CREATED)
                except IntegrityError as e:
                    return Response({'data':{},'status':False,'message':"Rows Alreday Exist"}, status=404)
            return Response({'data':serializer.errors,'status':True,'message':"fail"}, status=status.HTTP_400_BAD_REQUEST)



@api_view(['POST'])
@parser_classes([MultiPartParser, FormParser, JSONParser])
@permission_classes([IsAuthenticated])
def movetocart(request, format=None):
    if request.method == 'POST':
        serializer = AddProductToWishListSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            try:
                # GET product from wishlist(userFK,productFK)
                contact_detail = AddToWishlist.objects.get(userfk__id=request.data['userfk'],productfk__id=request.data['productfk'])

                # Check product in cart
                cart_product_detail =  AddToCart.objects.filter(userfk__id=request.data['userfk'],productfk__id=request.data['productfk'])
                print('cart_product_detail >>> ',cart_product_detail)
                # if exist product in cart
                if len(cart_product_detail)>0:
                    contact_detail.delete()
                    return Response({'data':"Item Successfully Moved to cart",'status':True,'message':"Moved to Cart"},status=200)
                # else product not exist in cart
                else:
                    serializer = AddToCartSerializer(data=request.data)
                    if serializer.is_valid(raise_exception=True):
                        try:
                            serializer.save()
                            contact_detail.delete()
                            return Response({'data':"Item Successfully Moved to cart",'status':True,'message':"Moved to Cart"},status=200)
                        except IntegrityError as e:
                            return Response({'data':{},'status':False,'message':"Rows Alreday Exist"}, status=404)
                       

            except AddToWishlist.DoesNotExist:
                return Response({'message': 'No Item Found! '},status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
@parser_classes([MultiPartParser, FormParser, JSONParser])
# @permission_classes([IsAuthenticated])
def wishlistproductsearch(request, format=None):
    if request.method == 'GET':
       if request.query_params.get('filterKey') == "searchbox":
        search_text = request.query_params.get('search_text')
        productData = ProductsListing.objects.filter(Q(productName__icontains=search_text))
        serializer = ProductsListingSerializer(productData, many=True)
        return Response({'data':serializer.data,'status':True,'message':"success"},  status=200)
    else:
        return Response("Please Provide Correct key Parameter")