import requests,json
# from .getAuthTokenKey import *


def getAuthToken(request):
    if request.session.has_key('auth_token'):
        auth_token_key = request.session['auth_token']
        print('auth_token_key : ',auth_token_key)
        return 'Token ' + auth_token_key 
    else:
        print('auth_token_key not avalaible')
        return None

def postMethod(request='',method='',task = '',pathInfo='',userName = '', userEmail = '',userPassword = '',dataList = []):
    tokenKey = getAuthToken(request)
    print('tokenKey >>> ',tokenKey)
    # ==================================    CUSTOMER REGISTRATION/LOGIN MODULE  ========================================
    # ==================================================================================================================
    if task == 'REGISTERCUSTOMER':
        payload= {
                'username': dataList['contact'],
                'password': dataList['password'],
                'first_name': dataList['fullname'],
                'mobileNO': dataList['contact'],
                'email': dataList['email']
                }
        payload = json.dumps(payload)
        headers = {
            # 'Authorization': tokenKey,
        'Content-Type': 'application/json'
        }
        url = pathInfo
        print('url >>> ',url)
        print('headers >>> ',headers)
        print('payload >>> ',payload)
        return requests.request(method, url, headers=headers, data=payload)


    elif task == 'LOGIN':
        payload= {
                'username': dataList['contact'],
                'password': dataList['password']
                }
        payload = json.dumps(payload)
        headers = {
            # 'Authorization': tokenKey,
        'Content-Type': 'application/json'
        }
        url = pathInfo
        print('url >>> ',url)
        print('headers >>> ',headers)
        print('payload >>> ',payload)
        return requests.request(method, url, headers=headers, data=payload)

    elif task == 'SENDOTP':
        payload= {
                'mobNO': dataList['mobNO']
                }
        payload = json.dumps(payload)
        headers = {
            # 'Authorization': tokenKey,
        'Content-Type': 'application/json'
        }
        url = pathInfo
        print('url >>> ',url)
        print('headers >>> ',headers)
        print('payload >>> ',payload)
        return requests.request(method, url, headers=headers, data=payload)

    elif task == 'VERIFYOTP':
        payload= {
                'mobNO': str(dataList['mobileNumber']),
                'user_enter_otp': str(dataList['otp'])
                }
        payload = json.dumps(payload)
        headers = {
            # 'Authorization': tokenKey,
        'Content-Type': 'application/json'
        }
        url = pathInfo
        print('url >>> ',url)
        print('headers >>> ',headers)
        print('payload >>> ',payload)
        return requests.request(method, url, headers=headers, data=payload)
    
    # ==================================================================================================================
    # ==================================================================================================================
    elif task == 'CREATEENQUIRY':
        payload= {
                'name': dataList['customerName'],
                'contactNo': dataList['customerContact'],
                'email': dataList['customerEmail'],
                'remarks': dataList['customerRemark'],
                'productfk': dataList['productID'],
                'userfk': dataList['userID'],
                'address': dataList['customerAddress'],
                 'state': dataList['custState'],
                  'city': dataList['custCity'],
                'status': 'Enquiry Initiated',

                }
        payload = json.dumps(payload)
        headers = {
            'Authorization': tokenKey,
        'Content-Type': 'application/json'
        }
        url = pathInfo
        print('url >>> ',url)
        print('headers >>> ',headers)
        print('payload >>> ',payload)
        return requests.request(method, url, headers=headers, data=payload)

    elif task == 'CREATECONTACT':
        payload= {
                'name': dataList['customerName'],
                'email': dataList['customerEmail'],
                'subject': dataList['Subject'],
                'remarks': dataList['review']
                }
        payload = json.dumps(payload)
        headers = {
            'Authorization': tokenKey,
        'Content-Type': 'application/json'
        }
        url = pathInfo
        print('url >>> ',url)
        print('headers >>> ',headers)
        print('payload >>> ',payload)
        return requests.request(method, url, headers=headers, data=payload)

    elif task == 'CREATENEWADDRESS':
        payload= {
                'fullname': dataList['fullname'],
                'contact': dataList['contact'],
                'district': dataList['district'],

                'address': dataList['address'],
                'landmark': dataList['location'],
                'state': dataList['state'],
                'pincode': dataList['pincode'],
                'userInstance': dataList['userID'],
                }
        payload = json.dumps(payload)
        headers = {
            'Authorization': tokenKey,
        'Content-Type': 'application/json'
        }
        url = pathInfo
        print('url >>> ',url)
        print('headers >>> ',headers)
        print('payload >>> ',payload)
        return requests.request(method, url, headers=headers, data=payload)

    elif task == 'UPDATEADDRESS':
        payload= {
                'fullname': dataList['fullname'],
                'contact': dataList['contact'],
                'district': dataList['district'],
                'address': dataList['address'],
                'landmark': dataList['landmark'],
                'state': dataList['state'],
                'pincode': dataList['pincode'],
                'userInstance': dataList['userID'],
                }
        payload = json.dumps(payload)
        headers = {
            'Authorization': tokenKey,
        'Content-Type': 'application/json'
        }
        url = pathInfo
        print('url >>> ',url)
        print('headers >>> ',headers)
        print('payload >>> ',payload)
        return requests.request(method, url, headers=headers, data=payload)

    elif task == 'UPDATEPROFILE':
        payload= {
                'emaiID': dataList['userEmail'],
                'mobileNO': dataList['userContact'],
                'user': dataList['userID']
                }
        payload = json.dumps(payload)
        headers = {
            'Authorization': tokenKey,
        'Content-Type': 'application/json'
        }
        url = pathInfo
        print('url >>> ',url)
        print('headers >>> ',headers)
        print('payload >>> ',payload)
        return requests.request(method, url, headers=headers, data=payload)

    elif task == 'ADDTOCART':
        payload= {
                'userfk': dataList['userID'],
                'productfk': dataList['productID'],
                }
        payload = json.dumps(payload)
        headers = {
            'Authorization': tokenKey,
        'Content-Type': 'application/json'
        }
        url = pathInfo
        print('url >>> ',url)
        print('headers >>> ',headers)
        print('payload >>> ',payload)
        return requests.request(method, url, headers=headers, data=payload)


    elif task == 'ADDTOWISHLIST':
        payload= {
                'userfk': dataList['userID'],
                'productfk': dataList['productID'],
                }
        payload = json.dumps(payload)
        headers = {
            'Authorization': tokenKey,
        'Content-Type': 'application/json'
        }
        url = pathInfo
        print('url >>> ',url)
        print('headers >>> ',headers)
        print('payload >>> ',payload)
        return requests.request(method, url, headers=headers, data=payload)



    elif task == 'CHECKCARTLIST':
        payload= {
                'userfk': dataList['userfk'],
                'productfk': dataList['productfk'],
                }
        payload = json.dumps(payload)
        headers = {
            'Authorization': tokenKey,
        'Content-Type': 'application/json'
        }
        url = pathInfo
        print('url >>> ',url)
        print('headers >>> ',headers)
        print('payload >>> ',payload)
        return requests.request(method, url, headers=headers, data=payload)

    elif task == 'CHECKWISHLIST':
        payload= {
                'userfk': dataList['userfk'],
                'productfk': dataList['productfk'],
                }
        payload = json.dumps(payload)
        headers = {
            'Authorization': tokenKey,
        'Content-Type': 'application/json'
        }
        url = pathInfo
        print('url >>> ',url)
        print('headers >>> ',headers)
        print('payload >>> ',payload)
        return requests.request(method, url, headers=headers, data=payload)

    elif task == 'MOVETOCART':
        payload= {
                'userfk': request.session['userID'],
                'productfk': dataList['productfk'],
                }
        payload = json.dumps(payload)
        headers = {
            'Authorization': tokenKey,
        'Content-Type': 'application/json'
        }
        url = pathInfo
        print('url >>> ',url)
        print('headers >>> ',headers)
        print('payload >>> ',payload)
        return requests.request(method, url, headers=headers, data=payload)

    elif task == 'REMOVECARTITEM':
        payload= {
                'userfk': dataList['userFk'],
                'productfk': dataList['productID'],
                'action' : 'remove'
                }
        payload = json.dumps(payload)
        headers = {
            'Authorization': tokenKey,
        'Content-Type': 'application/json'
        }
        url = pathInfo
        print('url >>> ',url)
        print('headers >>> ',headers)
        print('payload >>> ',payload)
        return requests.request(method, url, headers=headers, data=payload)


    elif task == 'UPDATECARTPRODUCTQUANTITY':
        payload= {
                'userfk': int(request.session['userID']),
                'productfk': int(dataList['productID']),
                'productQuantity': dataList['quantity']
                }
        payload = json.dumps(payload)
        headers = {
            'Authorization': tokenKey,
        'Content-Type': 'application/json'
        }
        url = pathInfo
        print('url >>> ',url)
        print('headers >>> ',headers)
        print('payload >>> ',payload)
        return requests.request(method, url, headers=headers, data=payload)

    # return 

    