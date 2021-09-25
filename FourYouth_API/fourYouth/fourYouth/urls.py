from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('fourYouthAPI.urls.homeUrl')),
    path('', include('fourYouthAPI.urls.aboutUsUrls')),
    path('', include('fourYouthAPI.urls.contactUsUrls')),
    path('', include('fourYouthAPI.urls.dashboardUrls')),
    path('', include('fourYouthAPI.urls.enquiryFormUrls')),
    path('', include('fourYouthAPI.urls.productListUrls')),
    path('', include('fourYouthAPI.urls.credentialUrl')),
    path('', include('fourYouthAPI.urls.userProfileUrls')),
    path('', include('fourYouthAPI.urls.searchDataUrls')),
    path('', include('fourYouthAPI.urls.addressUserUrls')),
    path('', include('fourYouthAPI.urls.addTocartUrls')),
    path('', include('fourYouthAPI.urls.orderDetailUrls')),
    path('', include('fourYouthAPI.urls.addProductToWishListUrls')),
    ]
