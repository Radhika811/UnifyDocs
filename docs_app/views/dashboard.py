from django.http import HttpResponse

def landing(request):
    return HttpResponse("This is the dashboard. If you reached here, you have successfully logged in with token authentication")