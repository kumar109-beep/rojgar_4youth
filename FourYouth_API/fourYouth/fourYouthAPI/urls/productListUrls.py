from ..views.productListViews import *
from django.urls import path

urlpatterns = [
    path('api/product_list/', product_list, name='product_list'),
    path('api/product_detail/<int:pk>/', product_detail, name='product_detail'),
    path('api/productCategory_list_web/', productCategory_list_web, name='productCategory_list_web'),
    path('api/productCategory_list/', productCategory_list, name='productCategory_list'),
    path('api/productCategory_detail/<int:pk>/', productCategory_detail, name='product_detail'),
    path('api/product_list_web/', product_list_web, name='product_list_web'),
    path('api/product_detail_web/<int:pk>/', product_detail_web, name='product_detail_web'),
    path('api/product_detail_related_web/<int:pk>/', product_detail_related_web, name='product_detail_related_web'),
    path('api/product_display_status/<int:pk>/', product_display_status, name='product_display_status'),
    path('api/filterproduct_web/', filterproduct_web, name='filterproduct_web')
]
