from ..views.searchDataViews import *
from django.urls import path

urlpatterns = [
    path('api/check_existing_data/', check_existing_data, name='check_existing_data'),
]
