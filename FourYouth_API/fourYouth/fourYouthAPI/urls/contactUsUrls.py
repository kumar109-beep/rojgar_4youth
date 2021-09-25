from ..views.contactUsViews import *
from django.urls import path

urlpatterns = [
    path('api/contactUs_list/', contactUs_list, name='contactUs_list'),
    path('api/contactUs_detail/<int:pk>/', contactUs_detail, name='contactUs_detail'),
    path('api/contactUs_list_web/', contactUs_list_web, name='contactUs_list_web'),
]
