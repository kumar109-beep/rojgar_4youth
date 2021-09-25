from ..views.addTocartViews import *
from django.urls import path

urlpatterns = [
    path('api/addTocart_list/', addTocart_list, name='addTocart_list'),
    path('api/addTocart_detail/<int:pk>/', addTocart_detail, name='addTocart_detail'),
    path('api/addTocartUser_list/<int:pk>/', addTocartUser_list, name='addTocartUser_list'),
    path('api/checkAdd_cart/', checkAdd_cart, name='checkAdd_cart'),
    path('api/checkCurrentlyAddOrNot/', checkCurrentlyAddOrNot, name='checkCurrentlyAddOrNot'),
    path('api/movetoWishlist/', movetoWishlist, name='movetoWishlist'),
]