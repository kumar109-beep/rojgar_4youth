from django.contrib import admin
from django.urls import path
from youth_rural_app.views import *

import random,string




urlpatterns = [
    path('admin/', admin.site.urls),

    path('',home,name='home'),
    # --------------------------------------    REGISTRATION & LOGIN Urls    ---------------------------------------
    path('customer-management/customer-signin',login,name='login'),
    path('send_OTP',send_OTP,name='send_OTP'),
    path('verifyOTP',verifyOTP,name='verifyOTP'),

    path('send_signup_OTP',send_signup_OTP,name='send_signup_OTP'),
    path('verifySignUpOTP',verifySignUpOTP,name='verifySignUpOTP'),


# 
    path('customer-management/register',register,name='register'),
    path('getExitiingUser',getExitiingUser,name='getExitiingUser'),
    path('logout',logout,name='logout'),
    # --------------------------------------------------------------------------------------------------------------
    path('customer-management/customer-info',customer_info,name='customer_info'),
    path('customer-management/customer-orders',customer_orders,name='customer_orders'),
    path('customer-management/customer-orders-detail',customer_order_detail,name='customer_order_detail'),

    path('customer-management/customer-address',customer_address,name='customer_address'),
    path('update_address',update_address,name='update_address'),

    path('about-us',about,name='about'),
    path('contact',contact,name='contact'),
    path('product-catalog',product_catalog,name='product_catalog'),
    path('product_search_filter',product_search_filter,name='product_search_filter'),
    path('loadMoreProducts',loadMoreProducts,name='loadMoreProducts'),


    path('product-detail/product-query/<int:id>',product_detail,name='product_detail'),
    path('product-detail/product-query/remove-product-from-cart/<int:id>',remove_product_from_cart,name='remove_product_from_cart'),

    path('create_enquiry',create_enquiry,name='create_enquiry'),
    path('product-cart',cart,name='cart'),
    path('product-checkout',checkout,name='checkout'),

    path('add-product-cart/<int:id>',add_to_cart,name='add_to_cart'),
    path('delete_cart_items/<int:id>',delete_cart_items,name='delete_cart_items'),
    path('update_cart_product_quantity',update_cart_product_quantity,name='update_cart_product_quantity'),

    path('wishlist',wishlist,name='wishlist'),
    path('add-wishlist-item/<int:id>',add_to_wishlist,name='add_to_wishlist'),
    path('deleteWishlistProducts/<int:id>',deleteWishlistProducts,name='deleteWishlistProducts'),
    path('MoveToCArt/<int:id>',MoveToCArt,name='MoveToCArt'),
    path('pdf/', GeneratePdf.as_view()),



]
# 