from ..views.enquiryFormViews import *
from django.urls import path

urlpatterns = [
    path('api/enquiryformdata_list_web/', enquiryformdata_list_web, name='enquiryformdata_list_web'),
    path('api/unique_customer/', unique_customer, name='unique_customer'),
    path('api/enquiryformdata_list/', enquiryformdata_list, name='enquiryformdata_list'),
    path('api/enquiryformdata_detail/<int:pk>/', enquiryformdata_detail, name='enquiryformdata_detail'),
    path('api/unique_customer_data/<int:pk>/', unique_customer_data, name='unique_customer_data'),
    path('api/enquiry_status/<int:userID>/', enquiry_status, name='enquiry_status'),
    
]
