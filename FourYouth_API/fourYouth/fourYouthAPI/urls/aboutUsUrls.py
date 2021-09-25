from ..views.aboutUsViews import *
from django.urls import path

urlpatterns = [
    path('api/aboutUs_list/', aboutUs_list, name='aboutUs_list'),
    path('api/aboutUs_detail/<int:pk>/', aboutUs_detail, name='aboutUs_detail'),
]
