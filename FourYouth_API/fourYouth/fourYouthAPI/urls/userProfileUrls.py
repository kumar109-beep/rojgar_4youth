from ..views.userProfileViews import *
from django.urls import path

urlpatterns = [
    path('api/userProfile_list/', userProfile_list, name='userProfile_list'),
    path('api/userProfile_detail/<int:pk>/', userProfile_detail, name='userProfile_detail'),
]
