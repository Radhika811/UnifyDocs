from rest_framework import viewsets
from docs_app.serializers import UserSerializer
from docs_app.models import User

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()