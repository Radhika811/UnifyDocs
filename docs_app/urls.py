from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from docs_app import views

router = DefaultRouter()
router.register(r'users', views.UserViewSet, basename='user')
# router.register(r'documents', views.document_list, basename='documents')
router.register(r'groups', views.GroupViewSet, basename='groups')
router.register(r'tags', views.TagViewSet, basename='tags')


urlpatterns = [
    path('', views.index, name = 'home'),
    path('oauth/authorize/', views.authorize, name='authorize'),
    path('login', views.auth.auth_token, name='token_exchange'),
    path('dashboard', views.landing),
    path('documents/', views.document_list, name='document-list'),
    path('documents/<int:pk>/', views.document_detail, name='document-detail'),

    # Custom views for document_list and document_detail
    

    
    # path('get_data', views.auth.get_data, name='get_data')
    # Add other URL patterns here as needed.f
]
urlpatterns += router.urls
