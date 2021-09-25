from ..views.addressUserViews import *
from django.urls import path

urlpatterns = [
    path('api/address_list/', address_list, name='address_list'),
    path('api/address_detail/<int:pk>/', address_detail, name='address_detail'),
    path('api/getAllAddressByUser/<int:pk>/', getAllAddressByUser, name='getAllAddressByUser'),
]
