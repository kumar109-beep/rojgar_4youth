from django.http.response import HttpResponse, JsonResponse,HttpResponseRedirect
from django.shortcuts import render,redirect

from.helper.getMethod import *
from.helper.postMethod import *
from.helper.globalURLS import *
import json

import razorpay
from youth_rural_web.settings import RAZORPAY_API_KEY,RAZORPAY_API_SECRET_KEY
# ===========================================================================
#                       REGISTRATION & LOGIN Views
# ===========================================================================
def login(request):
    if request.method == 'GET':
        if request.session.has_key('userID'):
            return redirect('home')
        else:
            if request.session.has_key('register'):
                del request.session['register']
                message = 'New Customer Registered Successfuly. Login to Continue.'
                return render(request,'web_login/login.html',{'message':message})
            else:
                return render(request,'web_login/login.html')


    if request.method == 'POST':
        contact = request.POST['contact']
        password = request.POST['password']

        print('contact >> ',contact)
        print('password >> ',password)

        data = {}
        data['contact'] = contact.strip()
        data['password'] = password.strip()

        apiRegisterCustomer = postMethod(
            request=request,
            method='POST',
            task = 'LOGIN',
            pathInfo=Login_URL.strip(),
            dataList = data
            )
        res = apiRegisterCustomer
        res = json.loads(res.text)
        print('response >>> ',res)
        # ========================================================
        try:
            # ------------- session data  --------------------------------
            request.session['userID'] = res['userProfileData']['id']
            request.session['mobileNO'] = res['userProfileData']['mobileNO']
            # request.session['birth_date'] = res['userProfileData']['birth_date']
            request.session['userFullName'] = res['userProfileData']['user']['first_name']
            request.session['email'] = res['userProfileData']['user']['email']
            request.session['username'] = 'Rojgar_ID_'+res['userProfileData']['user']['username']
            request.session['userProfileId'] = res['userProfileData']['user']['id']
            request.session['auth_token'] = res['token']
            # ------------------------------------------------------------
            if request.session.has_key('productUrl'):
                url = request.session['productUrl']
                print('url >>>>>>> ',url)
                return HttpResponseRedirect(url)
            else:
                return redirect('home')

        except:
            message = 'Invalid Username or Password!'
        # ========================================================
            return render(request,'web_login/login.html',{'error_message':message})
# -----------------------------------------------------------------------------
def register(request):
    if request.method == 'GET':
        try:
            if request.session.has_key('userID'):
                return redirect('home')
            else:
                return render(request,'web_login/login.html')
        except:
            return redirect('logout')

    if request.method == 'POST':
        fullname = request.POST['register_fullname']
        contact = request.POST['register_contact']
        email = request.POST['register_email']
        # dob = request.POST['register_dob']
        password = request.POST['register_password']

        print('fullname >> ',fullname)
        print('contact >> ',contact)
        print('email >> ',email)
        # print('dob >> ',dob)
        print('password >> ',password)

        data = {}
        data['fullname'] = fullname.strip()
        data['contact'] = contact.strip()
        data['email'] = email.strip()
        # data['dob'] = dob.strip()
        data['password'] = password.strip()


        apiRegisterCustomer = postMethod(
            request=request,
            method='POST',
            task = 'REGISTERCUSTOMER',
            pathInfo=customerRegistrationUrls.strip(),
            dataList = data
            )
        res = apiRegisterCustomer
        res = json.loads(res.text)
        print('response >>> ',res)
        message = ''
        if res['message'] == 'success':
            request.session['register'] = 'New customer added'
            return redirect('login')
        else:
            message = 'An Error Occured .Try Again!'


        return render(request,'web_login/login.html',{'message':message})

# ===========================================================================
#                       Customer Info Views
# ===========================================================================
def customer_info(request):
    if request.session.has_key('userID'):
        if request.method == 'GET':
            try:
                if request.session.has_key('productUrl'):
                    del request.session['productUrl']
                
                # =======================================================================================
                apiCartDetails = getMethod(
                request=request,
                method='GET',
                task = 'GETCARTLIST',
                pathInfo=cartDetail_URL+'/'+str(request.session['userID'])+'/'.strip(),
                )

                cart_detail = json.loads(apiCartDetails.text)
                print('>>>>>>>>>>>>>>>>>>>',cart_detail,len(cart_detail['data']))
                print('333333333333')
                # =======================================================================================
                return render(request,'web_customer/customer-info-page.html',{'cartLength':len(cart_detail['data'])})
            except:
                return redirect('logout')

        if request.method == 'POST':
            if request.session.has_key('productUrl'):
                del request.session['productUrl']

            userEmail = request.POST['userEmail']
            userContact = request.POST['userContact']

            print('userEmail >> ',userEmail)
            print('userContact >> ',userContact)

            data = {}
            data['userEmail'] = userEmail.strip()
            data['userContact'] = userContact.strip()
            data['userID'] = int(request.session['userProfileId'])

            apiUpdateProfile = postMethod(
                request=request,
                method='PUT',
                task = 'UPDATEPROFILE',
                pathInfo=updateProfile_URL+str(request.session['userID'])+'/'.strip(),
                dataList = data
                )
            res = json.loads(apiUpdateProfile.text)
            print('response >>> ',res)

            return JsonResponse({'responseData':res})
    else:
        return redirect('login')
# -----------------------------------------------------------------------------
def customer_orders(request):
    if request.session.has_key('userID'):
        if request.method == 'GET':
            try:
                if request.session.has_key('productUrl'):
                    del request.session['productUrl']
                apiProductList = getMethod(
                request=request,
                method='GET',
                task = 'GETORDERLIST',
                pathInfo=userOrderList_URL+str(request.session['userID'])+'/'.strip(),
                )

                productList = json.loads(apiProductList.text)
                print('>>>>>>>>>>>>>>>>>>>',productList)

                # =======================================================================================
                apiCartDetails = getMethod(
                request=request,
                method='GET',
                task = 'GETCARTLIST',
                pathInfo=cartDetail_URL+'/'+str(request.session['userID'])+'/'.strip(),
                )

                cart_detail = json.loads(apiCartDetails.text)
                print('>>>>>>>>>>>>>>>>>>>',cart_detail,len(cart_detail['data']))
                # 'cartLength':len(cart_detail['data'])
                # =======================================================================================
                return render(request,'web_customer/customers-order.html',{"orderData":productList['data'],'cartLength':len(cart_detail['data'])})
            except:
                return redirect('logout')

        if request.method == 'POST':
            if request.session.has_key('productUrl'):
                del request.session['productUrl']
            username = request.POST['username']
            password = request.POST['password']

            print('username >> ',username)
            print('password >> ',password)

            return render(request,'web_customer/customers-order.html')
    else:
        return redirect('login')
# -----------------------------------------------------------------------------
def customer_address(request):
    if request.session.has_key('userID'):
        if request.method == 'GET':
            try:
                if request.session.has_key('productUrl'):
                    del request.session['productUrl']
                
                apiAllAddressByUser = getMethod(
                request=request,
                method='GET',
                task = 'GETORDERLIST',
                pathInfo=getAllAddressByUser_URL+str(request.session['userID'])+'/'.strip(),
                )

                res = json.loads(apiAllAddressByUser.text)
                print('res >>>>>>>>',res)

                # =======================================================================================
                apiCartDetails = getMethod(
                request=request,
                method='GET',
                task = 'GETCARTLIST',
                pathInfo=cartDetail_URL+'/'+str(request.session['userID'])+'/'.strip(),
                )

                cart_detail = json.loads(apiCartDetails.text)
                print('>>>>>>>>>>>>>>>>>>>',cart_detail,len(cart_detail['data']))
                # 'cartLength':len(cart_detail['data'])
                # =======================================================================================
                return render(request,'web_customer/customer-Address.html',{'res':res['data'],'cartLength':len(cart_detail['data'])})
            except:
                return redirect('logout')

        if request.method == 'POST':
            if request.session.has_key('productUrl'):
                del request.session['productUrl']

            fullname = request.POST['fullname']
            contact = request.POST['contact']
            district = request.POST['district']
            address = request.POST['address']
            location = request.POST['location']
            state = request.POST['state']
            pincode = request.POST['pincode']

            data = {}
            data['fullname'] = fullname.strip()
            data['contact'] = contact.strip()
            data['district'] = district.strip()

            data['address'] = address.strip()
            data['location'] = location.strip()
            data['state'] = state.strip()
            data['pincode'] = pincode.strip()
            data['userID'] = int(request.session['userID'])

            apiCreateContact = postMethod(
                request=request,
                method='POST',
                task = 'CREATENEWADDRESS',
                pathInfo=addNewAddress_URL.strip(),
                dataList = data
                )
            res = json.loads(apiCreateContact.text)
            print('response >>> ',res)

            return JsonResponse({'responseData':res})
    else:
        return redirect('login')
# --------------------------------------------------------------------------
# -----------------------------------------------------------------------------
def update_address(request):
    if request.session.has_key('userID'):
        if request.method == 'POST':
            if request.session.has_key('productUrl'):
                del request.session['productUrl']

            fullname = request.POST['fullname']
            contact = request.POST['contact']
            district = request.POST['district']
            address = request.POST['address']
            landmark = request.POST['landmark']
            state = request.POST['state']
            pincode = request.POST['pincode']
            addressId = request.POST['id']

            data = {}
            data['fullname'] = fullname.strip()
            data['contact'] = contact.strip()
            data['district'] = district.strip()
            data['address'] = address.strip()
            data['landmark'] = landmark.strip()
            data['state'] = state.strip()
            data['pincode'] = pincode.strip()
            data['userID'] = int(request.session['userID'])

            apiCreateContact = postMethod(
                request=request,
                method='PUT',
                task = 'UPDATEADDRESS',
                pathInfo=updateAddress_URL+str(addressId)+'/'.strip(),
                dataList = data
                )
            res = json.loads(apiCreateContact.text)
            print('response >>> ',res)

            return JsonResponse({'responseData':res})
    else:
        return redirect('login')
# ===========================================================================
#                       Dashboard Views
# ===========================================================================
def home(request):
    if request.method == 'GET':
        try:
            if request.session.has_key('productUrl'):
                del request.session['productUrl']
            apiProductList = getMethod(
            request=request,
            method='GET',
            task = 'GETCATEGORYLIST',
            pathInfo=productList_URL.strip(),
            )

            productList = json.loads(apiProductList.text)
            print('>>>>>>>>>>>>>>>>>>>',productList)
            # ---------------------------------------------------------
            apiBanners = getMethod(
            request=request,
            method='GET',
            task = 'GETCATEGORYLIST',
            pathInfo=bannerList_URL.strip(),
            )

            bannerList = json.loads(apiBanners.text)
            print('>>>>>>>>>>>>>>>>>>>',bannerList)
            # ---------------------------------------------------------
            productListLength = len(productList)
            print('productListLength >>> ',productListLength)
            # =======================================================================================
            try:
                apiCartDetails = getMethod(
                request=request,
                method='GET',
                task = 'GETCARTLIST',
                pathInfo=cartDetail_URL+'/'+str(request.session['userID'])+'/'.strip(),
                )

                cart_detail = json.loads(apiCartDetails.text)
                print('>>>>>>>>>>>>>>>>>>>',cart_detail,len(cart_detail['data']))
                # 'cartLength':len(cart_detail['data'])
                return render(request,'web-templates/index.html',{'productList':productList['data'],'productListLength':productListLength,'bannerList':bannerList['data'],'cartLength':len(cart_detail['data'])})
                # =======================================================================================
            except:
                return render(request,'web-templates/index.html',{'productList':productList['data'],'productListLength':productListLength,'bannerList':bannerList['data']})
        except:
            return redirect('logout')

# ===========================================================================
#                       About section Views
# ===========================================================================
def about(request):
    if request.method == 'GET':
        try:
            if request.session.has_key('productUrl'):
                del request.session['productUrl']
            try:
                # =======================================================================================
                apiCartDetails = getMethod(
                request=request,
                method='GET',
                task = 'GETCARTLIST',
                pathInfo=cartDetail_URL+'/'+str(request.session['userID'])+'/'.strip(),
                )

                cart_detail = json.loads(apiCartDetails.text)
                print('>>>>>>>>>>>>>>>>>>>',cart_detail,len(cart_detail['data']))
                # 'cartLength':len(cart_detail['data'])
                # =======================================================================================
                return render(request,'web-templates/about.html',{'cartLength':len(cart_detail['data'])})
            except:
                return render(request,'web-templates/about.html')
        except:
            return redirect('logout')


# ===========================================================================
#                       Contact Us Views
# ===========================================================================
def contact(request):
    if request.method == 'GET':
        try:
            if request.session.has_key('productUrl'):
                del request.session['productUrl']
            try:
                # =======================================================================================
                apiCartDetails = getMethod(
                request=request,
                method='GET',
                task = 'GETCARTLIST',
                pathInfo=cartDetail_URL+'/'+str(request.session['userID'])+'/'.strip(),
                )

                cart_detail = json.loads(apiCartDetails.text)
                print('>>>>>>>>>>>>>>>>>>>',cart_detail,len(cart_detail['data']))
                # 'cartLength':len(cart_detail['data'])
                # =======================================================================================
                return render(request,'web-templates/contact-us.html',{'cartLength':len(cart_detail['data'])})
            except:
                return render(request,'web-templates/contact-us.html')
        except:
            return redirect('logout')
    if request.method == 'POST':
        if request.session.has_key('productUrl'):
            del request.session['productUrl']
        customerName = request.POST['customerName']
        customerEmail = request.POST['customerEmail']
        Subject= request.POST['Subject']
        review = request.POST.get('review')

        data = {}
        data['customerName'] = customerName.strip()
        data['customerEmail'] = customerEmail.strip()
        data['Subject'] = Subject.strip()
        data['review'] = review.strip()


        apiCreateContact = postMethod(
            request=request,
            method='POST',
            task = 'CREATECONTACT',
            pathInfo=createContactEnquiry_URL.strip(),
            dataList = data
            )
        res = apiCreateContact
        print('response >>> ',res.text)
        message = ''
        if(res.status_code == 201):
            message = 'Success'
        else:
            message = "Failed"

    return HttpResponse(message)


# ===========================================================================
#                       Product Catalogs Views
# ===========================================================================
def product_catalog(request):
    if request.method == 'GET':
        try:
            if request.session.has_key('productUrl'):
                del request.session['productUrl']
            apiProductList = getMethod(
            request=request,
            method='GET',
            task = 'GETCATEGORYLIST',
            pathInfo=productList_URL.strip(),
            )
            productList = json.loads(apiProductList.text)
            productListLength = len(productList)

            apiProductCategoryList = getMethod(
            request=request,
            method='GET',
            task = 'GETCATEGORYLIST',
            pathInfo=productCategoryList_URL.strip(),
            )
            productCategoryList = json.loads(apiProductCategoryList.text)
            print('productCategoryList >>>>>>>>>>>>>>>>>>>',productCategoryList)
            try:
                # =======================================================================================
                apiCartDetails = getMethod(
                request=request,
                method='GET',
                task = 'GETCARTLIST',
                pathInfo=cartDetail_URL+'/'+str(request.session['userID'])+'/'.strip(),
                )

                cart_detail = json.loads(apiCartDetails.text)
                print('>>>>>>>>>>>>>>>>>>>',cart_detail,len(cart_detail['data']))
                # 'cartLength':len(cart_detail['data'])
                # =======================================================================================
                return render(request,'web-templates/product-catalog.html',{'productList':productList['data'],'productListLength':productListLength,'cartLength':len(cart_detail['data']),'productCategoryList':productCategoryList['data']})
            except:
                return render(request,'web-templates/product-catalog.html',{'productList':productList['data'],'productListLength':productListLength,'productCategoryList':productCategoryList['data']})
        except:
            return redirect('logout')



# ===========================================================================
#                       Specific Product Views
# ===========================================================================
def product_detail(request,id):
    if request.method == 'GET':
        try:
            request.session['productUrl'] = '/product-detail/product-query/'+str(id)
            # if request.session.has_key('userID'):
            apiSpecificProduct = getMethod(
            request=request,
            method='GET',
            task = 'GETCATEGORYLIST',
            pathInfo=specificProduct_URL+str(id)+'/'.strip(),
            )

            product_detail = json.loads(apiSpecificProduct.text)

            dimension = product_detail['data']['productDimension'].split('|')
            length = dimension[0]
            breadth = dimension[1]
            height = dimension[2]

            apiRelatedProduct = getMethod(
            request=request,
            method='GET',
            task = 'GETCATEGORYLIST',
            pathInfo=relatedProduct_URL+str(product_detail['data']['productCategory']['id'])+'/'.strip(),
            )

            relatedProduct = json.loads(apiRelatedProduct.text)
            print('111111111')

            try:
                # ------------------------------------------------------------------
                dataDict = {}
                dataDict['userfk'] = request.session['userID']
                dataDict['productfk'] = id

                apiCheckItem = postMethod(
                            request=request,
                            method='GET',
                            task = 'CHECKCARTLIST',
                            pathInfo=check_cart_item_URL.strip(),
                            dataList = dataDict
                            )
                response = json.loads(apiCheckItem.text)
                print('apiCheckItem >> ',response)
                message = ''
                if(response['message'] == 'exist'):
                    message = 'exist'
                else:
                    message = 'not exist'
                print('22222222222')
                # ------------------------------------------------------------------
                apiCheckItem = postMethod(
                            request=request,
                            method='GET',
                            task = 'CHECKWISHLIST',
                            pathInfo=check_wish_item_URL.strip(),
                            dataList = dataDict
                            )
                response = json.loads(apiCheckItem.text)
                print('apiCheckItem >> ',response)
                wishlistMessage = ''
                if(response['message'] == 'exist'):
                    wishlistMessage = 'exist'
                else:
                    wishlistMessage = 'not exist'
                print('22222222222',wishlistMessage)
                
                # =======================================================================================
                apiCartDetails = getMethod(
                request=request,
                method='GET',
                task = 'GETCARTLIST',
                pathInfo=cartDetail_URL+'/'+str(request.session['userID'])+'/'.strip(),
                )

                cart_detail = json.loads(apiCartDetails.text)
                # =======================================================================================
                return render(request,'web-templates/product-detail.html',{'product_detail':product_detail['data'],'length':length,'breadth':breadth,'height':height,'relatedProduct':relatedProduct['data'],'productId':id,'cartLength':len(cart_detail['data']),'message':message,'wishlistMessage':wishlistMessage})
            except:
                print('444444444444')
                return render(request,'web-templates/product-detail.html',{'product_detail':product_detail['data'],'length':length,'breadth':breadth,'height':height,'relatedProduct':relatedProduct['data'],'productId':id})
        except:
            return redirect('logout')
            # else:
        #     return redirect('login')


def remove_product_from_cart(request,id):
    if request.method == 'GET':
        try:
            dataDict = {}
            dataDict['userFk'] = request.session['userID']
            dataDict['productID'] = id


            apiCartDetails = postMethod(
            request=request,
            method='GET',
            task = 'REMOVECARTITEM',
            pathInfo=removeCartItem_URL.strip(),
            dataList = dataDict
            )

            cart_detail = json.loads(apiCartDetails.text)
            return HttpResponseRedirect('/product-detail/product-query/'+str(id))
        except:
            return HttpResponseRedirect('/product-detail/product-query/'+str(id))

# ===========================================================================
#                       Product Enquiry Views
# ===========================================================================
def create_enquiry(request):
    if request.session.has_key('userID'):
        try:
            if request.session.has_key('productUrl'):
                    del request.session['productUrl']
            if request.method == 'POST':
                customerName = request.POST['customerName']
                customerContact = request.POST['customerContact']
                # customerAddress= request.POST['customerAddress']
                customerEmail = request.POST.get('customerEmail')
                customerRemark = request.POST.get('customerRemark')
                productID = request.POST['productID']
                customerAddress =  request.POST.get('customerAddress')
                custCity =  request.POST['custCity']
                custState =  request.POST['custState']
                data = {}
                data['customerName'] = customerName.strip()
                data['customerContact'] = customerContact.strip()
                data['customerEmail'] = customerEmail.strip()
                data['customerRemark'] = customerRemark.strip()
                data['productID'] = int(productID)
                data['userID'] = int(request.session['userID'])
                data['customerAddress'] = customerAddress.strip()
                data['custState'] = custState.strip()
                data['custCity'] = custCity.strip()
                apiCreateEnquiry = postMethod(
                    request=request,
                    method='POST',
                    task = 'CREATEENQUIRY',
                    pathInfo=createProductEnquiry_URL.strip(),
                    dataList = data
                    )
                res = apiCreateEnquiry
                print('response >>> ',res.text)
                message = ''
                if(res.status_code == 201):
                    message = 'Success'
                else:
                    message = "Failed"

            return HttpResponse(message)
        except:
            return redirect('logout')
    else:
        return redirect('login')

# ===========================================================================
#                       getExitiingUser Views
# ===========================================================================
def getExitiingUser(request):
    if request.method == 'GET':
        filter = request.GET['type_of_search']
        searchstring = request.GET['searchString']

        print('filter >> ',filter)
        print('searchString >> ',searchstring)

        apiGetExistingCustomer = getMethod(
        request=request,
        method='GET',
        task = 'GETCATEGORYLIST',
        pathInfo=getExistingCustomer_URL+"?type_of_search="+str(filter)+'&q='+str(searchstring).strip(),
        )

        apiGetExistingCustomer = json.loads(apiGetExistingCustomer.text)
        print('apiGetExistingCustomer >>> ',apiGetExistingCustomer)

        return JsonResponse({'responseData':apiGetExistingCustomer})



# ===========================================================================
#                       LOGOUT Views
# ===========================================================================
def logout(request):
    if request.method == 'GET':
        try:
            if request.session.has_key('userID'):
                del request.session['userID']
                del request.session['mobileNO']
                del request.session['birth_date']
                del request.session['email']
                del request.session['username']
                del request.session['userProfileId']
                del request.session['auth_token']

            if request.session.has_key('productUrl'):
                del request.session['productUrl']


        except KeyError:
            return redirect('login')
        return redirect('login')



client = razorpay.Client(auth=(RAZORPAY_API_KEY, RAZORPAY_API_SECRET_KEY))
def cart(request):
    if request.session.has_key('userID'):
        if request.method == 'GET':
            try:
                if request.session.has_key('productUrl'):
                    del request.session['productUrl']
                try:
                    order_amount = 50000
                    order_currency = 'INR'
                    order_receipt = 'order_rcptid_11'
                    payment_order = client.order.create(dict(amount=order_amount, currency=order_currency, receipt=order_receipt,payment_capture=1))
                    payment_order_id = payment_order['id']
                    context = {
                        'amount' : 500,
                        'api_key' : RAZORPAY_API_KEY,
                        'order_id' : payment_order_id
                    }
                    # =======================================================================================
                    apiCartDetails = getMethod(
                    request=request,
                    method='GET',
                    task = 'GETCARTLIST',
                    pathInfo=cartDetail_URL+'/'+str(request.session['userID'])+'/'.strip(),
                    )

                    cart_detail = json.loads(apiCartDetails.text)
                    print('>>>>>>>>>>>>>>>>>>>',cart_detail,len(cart_detail['data']))
                    # 'cartLength':len(cart_detail['data'])
                    totalPrice = 0
                    for i in cart_detail['data']:
                        amount = float(i['productfk']['productPrice'])*float(i['productQuantity'])
                        totalPrice = totalPrice + amount
                        print(totalPrice)

                    apiAllAddressByUser = getMethod(
                    request=request,
                    method='GET',
                    task = 'GETADDRESSLIST',
                    pathInfo=getAllAddressByUser_URL+str(request.session['userID'])+'/'.strip(),
                    )

                    addressList = json.loads(apiAllAddressByUser.text)
                    print('addressList >>>>>>>>',addressList)

                    # =======================================================================================

                    # =======================================================================================
                    return render(request,'web-templates/cart.html',{'cart_detail':cart_detail['data'],'cartLength':len(cart_detail['data']),'totalPrice':totalPrice,'addressList':addressList['data'],'context':context})
                except:
                    return render(request,'web-templates/cart.html')

            except:
                return redirect('logout')
    else:
        return redirect('login')



def add_to_cart(request,id):
    if request.session.has_key('userID'):
        if request.method == 'GET':
            try:
                print('product id >>> ',id)
                l1 = []
                data = {}
                data['userID'] = int(request.session['userID'])
                data['productID'] = id
                print(data)

                apiAddToCart = postMethod(
                    request=request,
                    method='POST',
                    task = 'ADDTOCART',
                    pathInfo=addTocart_list_URL.strip(),
                    dataList = data
                    )
                res = json.loads(apiAddToCart.text)
                print('response >>> ',res)

                if res['message']== 'success':
                    return HttpResponseRedirect('/product-detail/product-query/'+str(id))

                else:
                    return HttpResponseRedirect('/product-detail/product-query/'+str(id))
            except:
                return redirect('logout')
    else:
        return redirect('login')



def add_to_wishlist(request,id):
    if request.session.has_key('userID'):
        if request.method == 'GET':
            try:
                print('product id >>> ',id)
                l1 = []
                data = {}
                data['userID'] = int(request.session['userID'])
                data['productID'] = id
                print(data)

                apiAddToCart = postMethod(
                    request=request,
                    method='POST',
                    task = 'ADDTOWISHLIST',
                    pathInfo=addToWish_list_URL.strip(),
                    dataList = data
                    )
                res = json.loads(apiAddToCart.text)
                print('response >>> ',res)

                if res['message']== 'success':
                    return HttpResponseRedirect('/product-detail/product-query/'+str(id))

                else:
                    return HttpResponseRedirect('/product-detail/product-query/'+str(id))
            except:
                return redirect('logout')
    else:
        return redirect('login')


def delete_cart_items(request,id):
    if request.session.has_key('userID'):
        try:
            apiCartDetails = getMethod(
                    request=request,
                    method='DELETE',
                    task = 'GETCARTLIST',
                    pathInfo=delete_cart_item_URL+str(id)+'/'.strip(),
                    )
            print('apiCartDetails >> ',apiCartDetails.text)
            message = 'success'
        except:
            message = 'Failed'

        return JsonResponse({'message': message})
    else:
        return redirect('login')
    



def checkout(request):
    if request.session.has_key('userID'):
        try:
            # =======================================================================================
            apiCartDetails = getMethod(
            request=request,
            method='GET',
            task = 'GETCARTLIST',
            pathInfo=cartDetail_URL+'/'+str(request.session['userID'])+'/'.strip(),
            )

            cart_detail = json.loads(apiCartDetails.text)
            # print('>>>>>>>>>>>>>>>>>>>',cart_detail,len(cart_detail['data']))
            # 'cartLength':len(cart_detail['data'])
            totalPrice = 0
            for i in cart_detail['data']:
                amount = float(i['productfk']['productPrice'])*float(i['productQuantity'])
                totalPrice = totalPrice + amount
                # print(totalPrice)

            apiAllAddressByUser = getMethod(
            request=request,
            method='GET',
            task = 'GETADDRESSLIST',
            pathInfo=getAllAddressByUser_URL+str(request.session['userID'])+'/'.strip(),
            )

            addressList = json.loads(apiAllAddressByUser.text)
            # print('addressList >>>>>>>>',addressList)

            if totalPrice == 0:
                return redirect('cart')
            # =======================================================================================
            #                               RAZORPAY API INTEGRATION
            # =======================================================================================
            order_amount = totalPrice * 100
            order_currency = 'INR'
            order_receipt = 'order_rcptid_11'
            payment_order = client.order.create(dict(amount=order_amount, currency=order_currency, receipt=order_receipt,payment_capture=1))
            print('razor pay payment_order >>> ',payment_order)
            payment_order_id = payment_order['id']
            context = {
                'amount' : 500,
                'api_key' : RAZORPAY_API_KEY,
                'order_id' : payment_order_id
            }
            # =======================================================================================
            # =======================================================================================
            return render(request,'web-templates/checkout.html',{'cart_detail':cart_detail['data'],'cartLength':len(cart_detail['data']),'totalPrice':totalPrice,'addressList':addressList['data'],'context':context})
        except:
            return render(request,'web-templates/checkout.html')
    else:
        return redirect('login')




def customer_order_detail(request):
    if request.session.has_key('userID'):
        try:
            # =======================================================================================
            apiCartDetails = getMethod(
            request=request,
            method='GET',
            task = 'GETCARTLIST',
            pathInfo=cartDetail_URL+'/'+str(request.session['userID'])+'/'.strip(),
            )

            cart_detail = json.loads(apiCartDetails.text)
            print('>>>>>>>>>>>>>>>>>>>',cart_detail,len(cart_detail['data']))
            # 'cartLength':len(cart_detail['data'])
            totalPrice = 0
            for i in cart_detail['data']:
                amount = float(i['productfk']['productPrice'])
                totalPrice = totalPrice + amount
                print(totalPrice)

            apiAllAddressByUser = getMethod(
            request=request,
            method='GET',
            task = 'GETORDERLIST',
            pathInfo=getAllAddressByUser_URL+str(request.session['userID'])+'/'.strip(),
            )

            res = json.loads(apiAllAddressByUser.text)
            print('res >>>>>>>>',res)

            # if totalPrice == 0:
            #     return redirect('cart')
            # =======================================================================================
            order_amount = totalPrice * 100
            order_currency = 'INR'
            order_receipt = 'order_rcptid_11'
            payment_order = client.order.create(dict(amount=order_amount, currency=order_currency, receipt=order_receipt,payment_capture=1))
            payment_order_id = payment_order['id']
            context = {
                'amount' : 500,
                'api_key' : RAZORPAY_API_KEY,
                'order_id' : payment_order_id
            }

            # =======================================================================================
            return render(request,'web_customer/customer_order_detail.html',{'cart_detail':cart_detail['data'],'cartLength':len(cart_detail['data']),'totalPrice':totalPrice,'res':res['data'],'context':context})
        except:
            return render(request,'web_customer/customer_order_detail.html')
    else:
        return redirect('login')



def product_search_filter(request):
    if request.method == 'GET':
        categoryFilter = request.GET.getlist('categoryFilter[]')
        sortByFilter = request.GET['sortBy_Filter']
        priceRangeFilter = request.GET.getlist('priceRangeFilter[]')
        searchString = request.GET['search_String']
        filterKey = request.GET['filterKey']


        print('categoryFilter >>> ',categoryFilter)
        print('sortByFilter >>> ',sortByFilter)
        print('priceRangeFilter >>> ',priceRangeFilter)
        print('searchString >>> ',searchString)
        print('filterKey >>> ',filterKey)
        # ===============================================================================
        apiProductSearchFilter = getMethod(
            request=request,
            method='GET',
            task = 'SEARCHFILTERPRODUCT',
            pathInfo=productSearchFilter_URL+"?category_filter_data="+str(categoryFilter)+"&sortByPrice="+str(sortByFilter)+"&sortByPriceRange="+str(priceRangeFilter)+"&search_text="+str(searchString)+"&filterKey="+str(filterKey).strip(),
            )

        response = json.loads(apiProductSearchFilter.text)
        print('response >>>>>>>>',response)
        # ===============================================================================

        return JsonResponse({'filteredData':response})




def send_OTP(request):
    if request.method == 'POST':
        mobileNumber = request.POST['mobileNumber']
        data = {}
        data['mobNO'] = mobileNumber.strip()
        data['otpType'] = "Login".strip()

        apiSendOtp = postMethod(
            request=request,
            method='POST',
            task = 'SENDOTP',
            pathInfo=sendOtp_URL.strip(),
            dataList = data
            )
        res = apiSendOtp
        res = json.loads(res.text)
        print('response >>> ',res)

        return JsonResponse({'filteredData':res})



def verifyOTP(request):
    if request.method == 'POST':
        mobileNumber = request.POST['mobileNumber']
        otp = request.POST['otp']
        print('mobileNumber >> ',mobileNumber, len(mobileNumber))
        print('otp >> ',otp, len(otp))

        data = {}
        data['mobileNumber'] = mobileNumber.strip()
        data['otp'] = otp.strip()
        data['otpType'] = "Login".strip()


        apiVerifyOTP = postMethod(
            request=request,
            method='POST',
            task = 'VERIFYOTP',
            pathInfo=verifyOtp_URL.strip(),
            dataList = data
            )
        res = apiVerifyOTP
        res = json.loads(res.text)


        print('response >>> ',res)

        message = ''
        
        try:
            # ------------- session data  --------------------------------
            request.session['userID'] = res['userProfileData']['id']
            request.session['mobileNO'] = res['userProfileData']['mobileNO']
            # request.session['birth_date'] = res['userProfileData']['birth_date']
            request.session['email'] = res['userProfileData']['user']['email']
            request.session['username'] = 'Rojgar_ID_'+res['userProfileData']['user']['username']
            request.session['userProfileId'] = res['userProfileData']['user']['id']
            request.session['auth_token'] = res['token']
            # ------------------------------------------------------------
            # if request.session.has_key('productUrl'):
            #     url = request.session['productUrl']
            #     print('url >>>>>>> ',url)
            #     return HttpResponseRedirect(url)
            # else:
            #     return redirect('home')
            return JsonResponse({'responseData':res})

        except:
            message = 'Invalid Username or Password!'
            return JsonResponse({'responseData':res})
        # ========================================================


# ==========================================
def send_signup_OTP(request):
    if request.method == 'POST':
        mobileNumber = request.POST['mobileNumber']
        data = {}
        data['mobNO'] = mobileNumber.strip()
        data['otpType'] = "Signup".strip()

        apiSendOtp = postMethod(
            request=request,
            method='POST',
            task = 'SENDOTP',
            pathInfo=sendSignUpOtp_URL.strip(),
            dataList = data
            )
        res = apiSendOtp
        res = json.loads(res.text)
        print('response >>> ',res)

        return JsonResponse({'filteredData':res})



def verifySignUpOTP(request):
    if request.method == 'POST':
        mobileNumber = request.POST['mobileNumber']
        otp = request.POST['otp']
        print('mobileNumber >> ',mobileNumber, len(mobileNumber))
        print('otp >> ',otp, len(otp))

        data = {}
        data['mobileNumber'] = mobileNumber.strip()
        data['otp'] = otp.strip()
        data['otpType'] = "Signup".strip()


        apiVerifyOTP = postMethod(
            request=request,
            method='POST',
            task = 'VERIFYOTP',
            pathInfo=verifySignUpOtp_URL.strip(),
            dataList = data
            )
        res = apiVerifyOTP
        res = json.loads(res.text)


        print('response >>> ',res)
        return JsonResponse({'responseData':res})





def wishlist(request):
    if request.session.has_key('userID'):
        try:
            if request.method == 'GET':
                apiWishlistDetails = getMethod(
                    request=request,
                    method='GET',
                    task = 'GETCARTLIST',
                    pathInfo=Wishlist_list_URL+'/'+str(request.session['userID'])+'/'.strip(),
                    )

                wishlist_detail = json.loads(apiWishlistDetails.text)
                print('wishlist_detail >>>>>>>>>>>>>>>>>>>',wishlist_detail,len(wishlist_detail['data']))



                apiCartDetails = getMethod(
                    request=request,
                    method='GET',
                    task = 'GETCARTLIST',
                    pathInfo=cartDetail_URL+'/'+str(request.session['userID'])+'/'.strip(),
                    )

                cart_detail = json.loads(apiCartDetails.text)
                print('>>>>>>>>>>>>>>>>>>>',cart_detail,len(cart_detail['data']))
                return render(request,'web-templates/wishlist.html',{'wishlist_detail':wishlist_detail['data'],'wishlistLength':len(wishlist_detail['data']),'cart_detail':cart_detail['data'],'cartLength':len(cart_detail['data'])})
        except:
            return redirect('login')
    else:
        return redirect('login')


def deleteWishlistProducts(request,id):
    if request.session.has_key('userID'):
        try:
            apiWishlistDetails = getMethod(
                    request=request,
                    method='DELETE',
                    task = 'GETCARTLIST',
                    pathInfo=deleteWishlistProduct_URL+str(id)+'/'.strip(),
                    )
            print('apiWishlistDetails >> ',apiWishlistDetails.text)
            message = 'success'
        except:
            message = 'Failed'

        return JsonResponse({'message': message})
    else:
        return redirect('login')




def loadMoreProducts(request):
    if request.method == 'GET':
        pageNumber = request.GET['pageNo']

        apiCartDetails = getMethod(
            request=request,
            method='GET',
            task = 'GETPRODUCTLIST',
            pathInfo=productList_URL+'?page=' + str(pageNumber).strip(),
        )
        cart_detail = json.loads(apiCartDetails.text)
        print('>>>>>>>>>>>>>>>>>>>',cart_detail)
        return JsonResponse({'filteredData':cart_detail})




def update_cart_product_quantity(request):
    if request.method == 'POST':
        productID = request.POST['productID']
        recordID = request.POST['recordID']
        quantity = request.POST['productQuantity']


        data = {}
        data['productID'] = productID
        data['quantity'] = quantity


        apiSendOtp = postMethod(
            request=request,
            method='PUT',
            task = 'UPDATECARTPRODUCTQUANTITY',
            pathInfo=updateCart_URL+'/'+str(recordID)+'/'.strip(),
            dataList = data
            )
        res = apiSendOtp
        res = json.loads(res.text)
        print('response >>> ',res)

        return JsonResponse({'filteredData':res})


def MoveToCArt(request,id):
    if request.session.has_key('userID'):
        try:
            data = {}
            data['productfk'] = id

            print('data >>> ',data)


            apiSendOtp = postMethod(
                request=request,
                method='POST',
                task = 'MOVETOCART',
                pathInfo=moveToCart_URL.strip(),
                dataList = data
                )
            res = apiSendOtp
            res = json.loads(res.text)
            print('response >>>> ',res)
            return redirect('wishlist')

        except:
            return redirect('wishlist')
    else:
        return redirect('login')
# ============================================================================================================================
# ==========================================     INVOICE PDF     =========================================================
# ============================================================================================================================

from io import BytesIO
from django.template.loader import get_template
import xhtml2pdf.pisa as pisa

class Render:
    @staticmethod
    def render(path: str, params: dict):
        template = get_template(path)
        html = template.render(params)
        response = BytesIO()
        pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), response)
        if not pdf.err:
            return HttpResponse(response.getvalue(), content_type='application/pdf')
        else:
            return HttpResponse("Error Rendering PDF", status=400)


from django.views.generic import View
from django.utils import timezone
from datetime import date

class GeneratePdf(View):
    def get(self, request):
        today = date.today()
        params = {
            'Company_name' : 'YOUTH RURAL : Entrepreneur Foundation',
            'today_date': today,
            'request': request,
            'SNO':"YR-EF/2021102",
            'student_name' : 'Manohar Deshmukh',
            'student_rContact_number':'6758729809',
            # 'passing_status' : 'Passed',
            'Order_Array' : [{'product_name':'Produc 01','product_Price':100,'product_discounted_price':65,'product_Quantity':2},
                                {'product_name':'Product 02','product_Price':100,'product_discounted_price':55,'product_Quantity':1},
                                {'product_name':'Product 03','product_Price':100,'product_discounted_price':65,'product_Quantity':1},
                                {'product_name':'Product 04','product_Price':100,'product_discounted_price':65,'product_Quantity':1},
                                {'product_name':'Product 05','product_Price':100,'product_discounted_price':65,'product_Quantity':3}
                            ]
        }
        return Render.render('web_customer\customer_order_invoice.html', params)


# ================================================================================================================
# ================================================================================================================