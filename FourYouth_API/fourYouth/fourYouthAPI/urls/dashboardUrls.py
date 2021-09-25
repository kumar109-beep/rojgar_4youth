from ..views.dashboardViews import *
from django.urls import path

urlpatterns = [
    path('api/dashboard_list/', dashboard_list, name='dashboard_list'),
    path('api/dashboard_detail/<int:pk>/', dashboard_detail, name='dashboard_detail'),
    path('api/dashboard_count/', dashboard_count, name='dashboard_count'),
    path('api/dashboard_product/', dashboard_product, name='dashboard_product'),
    path('api/dashboard_enquiry/', dashboard_enquiry, name='dashboard_enquiry'),
    path('api/dashboard_list_web/', dashboard_list_web, name='dashboard_list_web'),  
]
