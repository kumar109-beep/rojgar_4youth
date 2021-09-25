import requests,json


def getAuthToken(request):
    if request.session.has_key('auth_token'):
        auth_token_key = request.session['auth_token']
        print('auth_token_key : ',auth_token_key)
        return 'Token ' + auth_token_key 
    else:
        print('auth_token_key not avalaible')
        return None

def getMethod(request='', method='',task = '',pathInfo='',dataList = []):
    tokenKey = getAuthToken(request)

    if task == 'GETCATEGORYLIST':
        payload = {}
        headers = {
            # 'Authorization': tokenKey,
        # 'Content-Type': 'application/json'
        }
        url = pathInfo
        print('api url info :------>> ',url)
        response = requests.request(method, url, headers=headers, data=payload)
        return response
        
    if task == 'GETPRODUCTLIST':
        payload = {}
        headers = {
            # 'Authorization': tokenKey,
        # 'Content-Type': 'application/json'
        }
        url = pathInfo
        print('api url info :------>> ',url)
        response = requests.request(method, url, headers=headers, data=payload)
        return response

    if task == 'SEARCHFILTERPRODUCT':
        payload = {}
        headers = {
            # 'Authorization': tokenKey,
        # 'Content-Type': 'application/json'
        }
        url = pathInfo
        print('api url info :------>> ',url)
        response = requests.request(method, url, headers=headers, data=payload)
        return response

    if task == 'GET_ALL_Language_List':
        payload = {}  
    if task == 'GETCARTLIST':
        payload = {}      
    if task == 'GETORDERLIST':
        payload = {}

    if task == 'GETADDRESSLIST':
        payload = {}
    
    ##########################################################################################
    headers = {
            'Authorization': tokenKey,
        # 'Content-Type': 'application/json'
        }
    url = pathInfo
    print('api url info :------>> ',url)
    response = requests.request(method, url, headers=headers, data=payload)
    return response






