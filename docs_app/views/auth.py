from django.shortcuts import redirect
import requests
from rest_framework.response import Response
from django.http import HttpResponse

access_token = ''
token_type = ''
# a = 2

def authorize(request):
    oauth_authorization_url = "https://channeli.in/oauth/authorise/?"
    oauth_params = {
        'client_id': 'C0krDWIFYdpPUXiom04ssVcWIfhWGRobrqz6BhyN',
        'redirect_uri': 'http://127.0.0.1:8000/login',
        'state': 'SECURE_STATE',
    }
    oauth_authorization_url += "&".join([f"{key}={value}" for key, value in oauth_params.items()])
    return redirect(oauth_authorization_url)

def auth_token(request):
    auth_token_url = "https://channeli.in/open_auth/token/"
    auth_token_params = {
        'client_id': 'C0krDWIFYdpPUXiom04ssVcWIfhWGRobrqz6BhyN',
        'client_secret': '3nZ6omkEB6QOZIbLRdJSzm4jbQUCBwHDeA6C13GDQH55JoprciyGmzYAnmxmMhJHlorUJf9TvqD5EaJB1R9z5OMHylXSMqQ5nDc7lc1lL5de8eRiyCt6hoLHa2e4PTaJ',
        'grant_type': 'authorization_code',
        'redirect_uri': 'http://127.0.0.1:8000/login',
        'code': request.GET.get('code'),
    }
    response = requests.post(auth_token_url, data = auth_token_params)
    # a+=5
    if response.status_code == 200:
        response_data = response.json()
        access_token = response_data.get("access_token")
        token_type = response_data.get("token_type")
        # print(a)
        print(response_data)
        
    else:
        print("Request failed with status code:", response.status_code)
        
    get_data_url = 'https://channeli.in/open_auth/get_user_data/'
    header = {
        'authorization': token_type + " " + access_token
    }
    response = requests.get(get_data_url, headers=header)
    if response.status_code == 200:
        response_data = response.json()
        print(response_data)
        return HttpResponse("User Data received successfully!!")
    print("Request failed with status code: ", response.status_code)
    return HttpResponse("Request failed due to status code : ", response.status_code)

# def get_data(request):
#     get_data_url = 'https://channeli.in/open_auth/get_user_data/'
#     header = {
#         'authorization': token_type + " " + access_token
#     }
#     response = requests.get(get_data_url, header=header)
#     if response.status_code == 200:
#         response_data = response.json()
#         print(response_data)
#         return HttpResponse("User Data received successfully!!")
#     print("Request failed with status code: ", response.status_code)
#     return HttpResponse("Request failed due to status code : ", response.status_code)
        
    
