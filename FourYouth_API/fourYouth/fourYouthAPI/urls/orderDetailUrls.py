from ..views.orderDetailViews import *
from django.urls import path

urlpatterns = [
    path('api/OrderDetail_list/', OrderDetail_list, name='OrderDetail_list'),
    path('api/OrderDetail_detail/<int:pk>/', OrderDetail_detail, name='OrderDetail_detail'),
]