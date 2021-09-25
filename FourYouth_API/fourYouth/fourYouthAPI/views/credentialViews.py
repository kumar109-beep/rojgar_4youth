from rest_framework import generics, permissions
from rest_framework.response import Response
from knox.models import AuthToken
# from ..models.credentialModel import *
from ..serializers.credentialSerializers import *
from django.contrib.auth import login
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from django.dispatch import receiver
from django.urls import reverse
from django_rest_passwordreset.signals import reset_password_token_created
from django.core.mail import send_mail
from rest_framework.pagination import PageNumberPagination
from django.http import QueryDict
import random
import string
import math
import requests
from django.http import HttpResponse
from ..models import *


#Custom Import
from ..serializers.credentialSerializers import *
from ..serializers.userProfileSerializers import *


# Register API
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    permission_classes = (permissions.AllowAny,)
    def post(self, request, *args, **kwargs):
        print('register API')
        userProfileModelDict = {}
        data = request.data
        if isinstance(request.data, QueryDict):
            data = dict(zip(request.data.keys(), request.data.values()))
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        if(len(data['mobileNO']) != 10):
            print(len(data['mobileNO']),data['mobileNO'])
            return Response({'data':{},'status':False,'message':"Invalid Contact Number.Contact length must be 10"}, status=400)
        user = serializer.save()
        userID = User.objects.latest('id')

        userProfileModelDict['user'] = userID.id
        userProfileModelDict["mobileNO"] = data['mobileNO']
        # userProfileModelDict["birth_date"] = data['birth_date']
        serializer = UserProfileSerializer(data=userProfileModelDict)
        if serializer.is_valid():
            serializer.save()
            return Response({
            "token": AuthToken.objects.create(user)[1],
            "userProfileData":serializer.data,
            "status":True,
            "message":"success"
            })
        else:
            inst = User.objects.get(id=userID.id)
            inst.delete()
            return Response({'data':serializer.errors,'status':True,'message':"fail"}, status=400)



'''

{
    "username": "admin",
    "email": "admin@bot.com",
    "password": "Password@123"
}


'''


class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)
    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        

        login(request, user)
        dataAdmin = UserSerializer(user).data
        try:
            user_data = UserProfile.objects.get(user__id=dataAdmin['id'])
            serializer = GETUserProfileSerializer(user_data)
            return Response({
            "userProfileData":serializer.data,
            "token": AuthToken.objects.create(user)[1],
            "status":True,
            "message":"success"
            })
        except UserProfile.DoesNotExist:
            return Response({'message': 'You are not correct user'},status=status.HTTP_404_NOT_FOUND)
        
        
class LoginAPIViaOTP(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)
    def post(self, request, format=None):
        try:
            OTPs = send_otp(request.data['mobNO'])
            UserProfile.objects.get(mobileNO=request.data['mobNO'])

            if(OtpDbModel.objects.filter(mobNO=request.data['mobNO'])):
                OtpDbModel.objects.get(mobNO=request.data['mobNO']).delete()

            data = OtpDbModel(mobNO=request.data['mobNO'],otpCode=OTPs)
            data.save()
            return Response({
            "mobileVerificationOTP":OTPs,
            "status":True,
            "message":"user verified"
            })
        except UserProfile.DoesNotExist:
            return Response({
            "mobileVerificationOTP":'',
            "status":False,
            "message":"Your Mobile Number is not correct"
            },status=status.HTTP_404_NOT_FOUND)



class LoginAPIViaOTPVerify(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)
    def post(self, request, format=None):
        try:
            data = OtpDbModel.objects.get(mobNO = request.data['mobNO'])
            dataOTP = data.otpCode
            print(dataOTP)
            user_enter_otp = request.data['user_enter_otp']
            if dataOTP == user_enter_otp:
                instanceUser = UserProfile.objects.get(mobileNO=request.data['mobNO'])
                user = User.objects.get(username=instanceUser.user.username)
                dataAdmin = UserSerializer(user).data

                user_data = UserProfile.objects.get(user__id=dataAdmin['id'])
                serializer = GETUserProfileSerializer(user_data)

                data = OtpDbModel.objects.get(mobNO=request.data['mobNO']).delete()

                
                return Response({
                "userProfileData":serializer.data,
                "token": AuthToken.objects.create(user)[1],
                "status":True,
                "message":"success"
                })
            else:
                return Response({'message': 'You have entered wrong otp code'},status=status.HTTP_404_NOT_FOUND)
        except:
            return Response({'message': 'OTP Expire'},status=status.HTTP_404_NOT_FOUND)








class SignUpAPIViaOTP(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)
    def post(self, request, format=None):
        try:
            OTPs = send_otp(request.data['mobNO'])
            # UserProfile.objects.get(mobileNO=request.data['mobNO'])

            if(OtpDbModel.objects.filter(mobNO=request.data['mobNO'])):
                OtpDbModel.objects.get(mobNO=request.data['mobNO']).delete()

            data = OtpDbModel(mobNO=request.data['mobNO'],otpCode=OTPs)
            data.save()
            return Response({
            "mobileVerificationOTP":OTPs,
            "status":True,
            "message":"user verified"
            })
        except UserProfile.DoesNotExist:
            return Response({
                "data":"",
                "status":False,
                "message":"Your Mobile Number is not correct"
                },status=status.HTTP_404_NOT_FOUND)



class SignUpAPIViaOTPVerify(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)
    def post(self, request, format=None):
        try:
            data = OtpDbModel.objects.get(mobNO = request.data['mobNO'])
            dataOTP = data.otpCode
            user_enter_otp = request.data['user_enter_otp']

            if dataOTP == user_enter_otp:
                data = OtpDbModel.objects.get(mobNO=request.data['mobNO']).delete()
                return Response({
                "data":"Mobile Number Verified",
                "status":True,
                "message":"success"
                })
            else:
                return Response({
                "data":"",
                "status":False,
                "message":"Invalid OTP"
                },status=status.HTTP_404_NOT_FOUND)
        except:
            return Response({
                "data":"",
                "status":False,
                "message":"OTP Expire"
                },status=status.HTTP_404_NOT_FOUND)
   

	
def rand_pass(size):
    digits = "0123456789"
    OTP = ""
    for i in range(4) :
        OTP += digits[math.floor(random.random() * 10)]
    return OTP


def send_otp(mobNo):
    otp = rand_pass(8)
    receiver = mobNo
    url = "https://www.fast2sms.com/dev/bulk"
    payload = "sender_id=FSTSMS&message=" + otp +"&language=english&route=p&numbers=" + str(receiver)
    headers = {
    'authorization': "jqwnLu1gNYIoptUykbHaPlKBV4D58E7srcXQFWhZS9zMJCxe6mPj8fE4ZxNbQtawTGgO19k5vA3XrCqm",
    'Content-Type': "application/x-www-form-urlencoded",
    'Cache-Control': "no-cache",
    }
    response = requests.request("POST", url, data=payload, headers=headers)
    return otp
       

    


class ChangePasswordView(generics.UpdateAPIView):
    """
    An endpoint for changing password.
    """
    serializer_class = ChangePasswordSerializer
    model = User
    permission_classes = (IsAuthenticated,)

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            # Check old password
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
            # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Password updated successfully',
                'data': []
            }

            return Response(response)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):

    # email_plaintext_messagess = "{}?token={}".format(reverse('password_reset:reset-password-request'), reset_password_token.key)
    email_plaintext_message = "{}?token={}".format(
        'http://localhost:5000/reset-your-password/', reset_password_token.key)
    send_mail(
        # title:
        "Password Reset for {title}".format(title="Some website title"),
        # message:
        email_plaintext_message,
        # from:
        "aditya.18pixels@gmail.com",
        # to:
        [reset_password_token.user.email]
    )
