from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'home'),
    path('oauth/authorize/', views.authorize, name='authorize'),
    path('login', views.auth.auth_token, name='token_exchange'),
    path('dashboard', views.landing)
    # path('get_data', views.auth.get_data, name='get_data')
    
    # Add other URL patterns here as needed.
]
