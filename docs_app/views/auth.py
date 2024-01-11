from django.shortcuts import redirect
import requests
from rest_framework.response import Response
from django.http import HttpResponse
from django.http import JsonResponse
from docs_app.models import User
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, authentication_classes, permission_classes
    
client_id = 'C0krDWIFYdpPUXiom04ssVcWIfhWGRobrqz6BhyN',
CLIENT_SECRET = "3nZ6omkEB6QOZIbLRdJSzm4jbQUCBwHDeA6C13GDQH55JoprciyGmzYAnmxmMhJHlorUJf9TvqD5EaJB1R9z5OMHylXSMqQ5nDc7lc1lL5de8eRiyCt6hoLHa2e4PTaJ"

def auth(name, year, role, enrollment, gender):
    print(name)
    try:
        print("and this worked?")
        user = User.objects.get(enrollment=enrollment)
        
        return user

    except User.DoesNotExist:
        print("Hi, reached here")
        User.objects.create(name=name, role=role,
                            year=year, enrollment=enrollment, gender=gender)
        user = User.objects.get(enrollment=enrollment)
        return user
    
@api_view(('GET',))
def authorize(request):
    oauth_authorization_url = "https://channeli.in/oauth/authorise/?"
    oauth_params = {
        'client_id': 'C0krDWIFYdpPUXiom04ssVcWIfhWGRobrqz6BhyN',
        'redirect_uri': 'http://127.0.0.1:8000/login',
        'state': 'SECURE_STATE',
    }
    oauth_authorization_url += "&".join([f"{key}={value}" for key, value in oauth_params.items()])
    return redirect(oauth_authorization_url)

@api_view(('GET', 'POST',))
@authentication_classes([])
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
    if response.status_code != 200:
        return HttpResponse("Error")

    response_data = response.json()
    access_token = response_data.get("access_token")
    token_type = response_data.get("token_type")
    print(response_data)   
    get_data_url = 'https://channeli.in/open_auth/get_user_data/'
    header = {
        'authorization': token_type + " " + access_token
    }
    response = requests.get(get_data_url, headers=header)
    print(response.json())
    if response.status_code == 200:
        response_data = response.json()
        
        role = response_data.get("person", {}).get("roles", "")
        print("reached here")
        maintainer = False
        for data in role:
            if(data['role'] == 'Maintainer'):
                maintainer = True
                
        if not maintainer:
            return HttpResponse("Only IMG members can use the site")

        try:
            username = response_data['username']
            existing_user = User.objects.get(enrollment = username)
            existing_user.year = response_data['student']['currentYear']
            existing_user.email = response_data['contactInformation']['instituteWebmailAddress']
            existing_user.phone_no = response_data['contactInformation']['primaryPhoneNumber']
            
            existing_user.save()
            token = Token.objects.get(user=existing_user)
            print(token.key)
            token_key = token.key
            user = existing_user
            
        except:
            new_user = User.objects.create(
                enrollment = response_data['username'],
                username = response_data['username'],
                password = 'password',
                name = response_data['person']['fullName'],
                year = response_data['student']['currentYear'],
                email = response_data['contactInformation']['instituteWebmailAddress'],
                phone_no = response_data['contactInformation']['primaryPhoneNumber'],
                gender = response_data['biologicalInformation']['sex']
            )
            new_user.is_staff = True
            new_user.save()
            print(new_user)
            token = Token.objects.create(user=new_user)
            print(token.key)
            token_key = token.key
            user = new_user
            
        user = User.objects.get(enrollment = username)
        print("user")
        token = Token.objects.get(user = user)
        authtoken = token.key
        userId = user.id 
        return redirect('http://localhost:3000/dashboard/?auth_token=' + authtoken + '&userid=' + str(userId) + '&username=' + user.name)
    
    print("Request failed with status code: ", response.status_code)
    return HttpResponse("Request failed due to status code : ", response.status_code)
