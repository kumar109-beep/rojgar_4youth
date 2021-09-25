from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from rest_framework.decorators import api_view,permission_classes,authentication_classes,parser_classes
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from knox.auth import TokenAuthentication
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from django.http import QueryDict
from django.core.mail import send_mail
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
import requests

# Custome Import
from ..serializers.enquiryFormSerializers import *

@api_view(['GET', 'POST'])
@parser_classes([MultiPartParser, FormParser, JSONParser])
@permission_classes([IsAuthenticated])
def enquiryformdata_list(request, format=None):
    if request.method == 'GET':
        paginator = PageNumberPagination()
        snippets = EnquiryFormData.objects.all().order_by('-created_at')
        snippets = paginator.paginate_queryset(snippets, request)
        serializer = GETEnquiryFormDataSerializer(snippets, many=True)
        return Response({'data':serializer.data,'status':True,'message':'success'},status=200)



@api_view(['GET','PUT','DELETE'])
@parser_classes([MultiPartParser, FormParser, JSONParser])
@permission_classes([IsAuthenticated])
def enquiryformdata_detail(request, pk, format=None):
    try:
        batchDetail = EnquiryFormData.objects.get(pk=pk)
    except EnquiryFormData.DoesNotExist:
        return Response({'message': 'Enquiry Not Found! '},status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = GETEnquiryFormDataSerializer(batchDetail)
        return JsonResponse({'data':serializer.data,'status':True,'message':'success'}, status=200, safe=False)

    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = EnquiryFormDataSerializer(batchDetail, data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse({'data':serializer.errors,'status':True,'message':'fail'}, status=400)

    elif request.method == 'DELETE':
        batchDetail.delete()
        return Response({'data':{"Deleted"},'status':True,'message':'success'},status=status.HTTP_204_NO_CONTENT)



@api_view(['GET', 'POST'])
@parser_classes([MultiPartParser, FormParser, JSONParser])
@permission_classes([IsAuthenticated])
def enquiryformdata_list_web(request, format=None):
    if request.method == 'POST':
        data = request.data
        if isinstance(request.data, QueryDict):
            data = dict(zip(request.data.keys(), request.data.values()))
        try:
            batchDetail = EnquiryForm.objects.get(contactNo=str(data['contactNo']))
            data['enquiryfk'] = batchDetail.id
            serializer = EnquiryFormDataSerializer(data=data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                send_otp()
                flag = sendingEmail("ADITYA SHUKLA","7355177189","adityashukla727@gmail.com")
                if flag == 'Mail_Send':
                    return Response({'data':serializer.data,'message':'Your Enquiry Submitted Successfully.','status':True}, status=201)
                else:
                    return Response({'data':serializer.data,'message':'Your Enquiry Submitted Successfully.','status':True}, status=201)
            return Response({'data':serializer.errors,'status':True,'message':'fail'},status=status.HTTP_404_NOT_FOUND)

        except EnquiryForm.DoesNotExist:
            formData = {}
            formData['contactNo'] = data['contactNo']
            serializer_one = EnquiryFormSerializer(data=formData)
            if serializer_one.is_valid():
                serializer_one.save()
                data['enquiryfk'] = serializer_one.data['id']
                serializer = EnquiryFormDataSerializer(data=data)
                if serializer.is_valid():
                    serializer.save()
                    send_otp()
                    flag = sendingEmail("ADITYA SHUKLA","7355177189","adityashukla727@gmail.com")
                    if flag == 'Mail_Send':
                        return Response({'data':serializer.data,'message':'Your Enquiry Submitted Successfully.','status':True}, status=201)
                    else:
                        return Response({'data':serializer.data,'message':'Your Enquiry Submitted Successfully.','status':True}, status=201)
                    
                return Response({'message': 'Data Format Not Valid! '},status=status.HTTP_404_NOT_FOUND)
            return Response({'data':serializer.errors,'status':True,'message':'fail'},status=status.HTTP_404_NOT_FOUND)



def sendingEmail(registrationNo,contactNo,email):
    subject, from_email, to = 'hello', settings.EMAIL_HOST_USER, email.strip()
    text_content = 'This is an important message.'
    html_content = '<!DOCTYPE html>\
        <html lang="en">\
        <head>\
        <title>Bootstrap Example</title>\
        <meta charset="utf-8">\
        <meta name="viewport" content="width=device-width, initial-scale=1">\
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">\
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>\
        <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.16.0/umd/popper.min.js"></script>\
        <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>\
        </head>\
        <body>\
        <div class="container" style="background-color:white;">\
        <div class="jumbotron" style="background-color:white;">\
            <h1><img src="http://13.233.247.133:8000/static/adminModule/images/logo.png" /></h1>\
            <p>Hello, Welcome to Slateo, your username '+ str(registrationNo) +'  and '+ str(contactNo) +' </p>\
        </div>\
        </div>\
        </body>\
        </html>'
    
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alternative(html_content, "text/html")
    try:
        msg.send()
        return "Mail_Send"
    except:
        return "Mail_Not_Send"



@api_view(['GET', 'POST'])
@parser_classes([MultiPartParser, FormParser, JSONParser])
@permission_classes([IsAuthenticated])
def unique_customer(request, format=None):
    if request.method == 'GET':
        paginator = PageNumberPagination()
        snippets1 = EnquiryForm.objects.all().order_by('-created_at')
        snippets = paginator.paginate_queryset(snippets1, request)
        serializer = GETEnquiryFormSerializer(snippets, many=True)
        return Response({'data':serializer.data,'status':True,'message':"success"}, status=200)
  

@api_view(['GET','PUT','DELETE'])
@parser_classes([MultiPartParser, FormParser, JSONParser])
@permission_classes([IsAuthenticated])
def unique_customer_data(request, pk, format=None):
    batchDetail = EnquiryFormData.objects.filter(enquiryfk__id=pk).order_by('-created_at')
    serializer = GETEnquiryFormDataSerializer(batchDetail, many=True)
    return JsonResponse({'data':serializer.data,'status':True,'message':'success'}, status=200, safe=False)




def send_otp():
    otp = "7355177189"
    receiver = "7355177189"
    url = "https://www.fast2sms.com/dev/bulk"
    payload = "sender_id=FSTSMS&message=" + str(otp) +"&language=english&route=p&numbers=" + str(receiver)
    headers = {
    'authorization': "QDo5cIdOBq6xG8YygsMkleWt7FAbXpjhimvZPz4J0VunCNEUf1D9H8ugEpaBMfK3FnwOhojeyZQXTWJm",
    'Content-Type': "application/x-www-form-urlencoded",
    'Cache-Control': "no-cache",
    }
    response = requests.request("POST", url, data=payload, headers=headers)
    return JsonResponse({'contact_data': receiver, 'msg': 'Success'})


@api_view(['GET', 'POST'])
@parser_classes([MultiPartParser, FormParser, JSONParser])
@permission_classes([IsAuthenticated])
def enquiry_status(request, userID,format=None):
    if request.method == 'GET':
        paginator = PageNumberPagination()
        snippets1 = EnquiryFormData.objects.filter(userfk__id=userID).order_by('-created_at')
        snippets = paginator.paginate_queryset(snippets1, request)
        serializer = GETEnquiryFormDataSerializer(snippets, many=True)
        return Response({'data':serializer.data,'status':True,'message':"success"}, status=200)
