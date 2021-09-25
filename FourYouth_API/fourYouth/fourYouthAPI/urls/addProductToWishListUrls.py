from ..views.addProductToWishListViews import *
from django.urls import path

urlpatterns = [
    path('api/addToWishlist_list/', addToWishlist_list, name='addToWishlist_list'),
    path('api/addToWishlist_detail/<int:pk>/', addToWishlist_detail, name='addToWishlist_detail'),
    path('api/CheckAdd_wishlist/', CheckAdd_wishlist, name='CheckAdd_wishlist'),
    path('api/checkCurrentlyAddOrNotproduct/', checkCurrentlyAddOrNotproduct, name='checkCurrentlyAddOrNotproduct'),
    path('api/movetocart/', movetocart, name='movetocart'),
    path('api/wishlistproductsearch/', wishlistproductsearch, name='wishlistproductsearch'),
]