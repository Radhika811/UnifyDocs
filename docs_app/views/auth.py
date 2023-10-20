from django.shortcuts import redirect

def authorize(request):
    oauth_authorization_url = "https://channeli.in/oauth/authorise/?"
    oauth_params = {
        'client_id': 'C0krDWIFYdpPUXiom04ssVcWIfhWGRobrqz6BhyN',
        'redirect_uri': 'http://127.0.0.1:8000/login',
        'state': 'SECURE_STATE',
    }
    oauth_authorization_url += "&".join([f"{key}={value}" for key, value in oauth_params.items()])
    return redirect(oauth_authorization_url)
