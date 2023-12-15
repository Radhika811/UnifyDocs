from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter
from docs_app import views

router = DefaultRouter()
router.register(r'users', views.UserViewSet, basename='user')
router.register(r'documents', views.DocumentViewSet, basename='documents')
router.register(r'groups', views.GroupViewSet, basename='groups')
router.register(r'tags', views.TagViewSet, basename='tags')
urlpatterns = router.urls

urlpatterns += [
    path('', views.index, name = 'home'),
    path('oauth/authorize/', views.authorize, name='authorize'),
    path('login', views.auth.auth_token, name='token_exchange'),
    path('dashboard', views.landing),

    
    # path('get_data', views.auth.get_data, name='get_data')
    # Add other URL patterns here as needed.f
]
