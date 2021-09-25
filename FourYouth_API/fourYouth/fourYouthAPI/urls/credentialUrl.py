# from django.urls import path
# from .views.credentialViews import *
# from rest_framework.urlpatterns import format_suffix_patterns

# urlpatterns = [
#     path('saltoSign/', Saleto_User_List),
#     path('checkExistingAccount/', checkExistingAccount),
#     path('saltoSign/<int:pk>/', Saleto_User_Detail),
# ]

# urlpatterns = format_suffix_patterns(urlpatterns)


from ..views.credentialViews import *
from django.urls import path,include
from knox import views as knox_views

urlpatterns = [
    path('api/register/', RegisterAPI.as_view(), name='register'),
    path('api/login/', LoginAPI.as_view(), name='login'),
    path('api/loginviaotp/', LoginAPIViaOTP.as_view(), name='loginviaotp'),
    path('api/loginviaVerifyotp/', LoginAPIViaOTPVerify.as_view(), name='loginviaVerifyotp'),
    path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
    path('api/change-password/', ChangePasswordView.as_view(), name='change-password'),
    path('api/password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
    path('api/signUPviaotp/', SignUpAPIViaOTP.as_view(), name='signUPviaotp'),
    path('api/signUPviaVerifyotp/', SignUpAPIViaOTPVerify.as_view(), name='signUPviaVerifyotp'),
]

