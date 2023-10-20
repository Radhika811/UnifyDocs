from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'home'),
    path('oauth/authorize/', views.authorize, name='authorize'),
    # Add other URL patterns here as needed.
]
