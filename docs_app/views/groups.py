from rest_framework import viewsets
from docs_app.serializers import GroupSerializer
from docs_app.models import Groups

class GroupViewSet(viewsets.ModelViewSet):
    serializer_class = GroupSerializer
    queryset = Groups.objects.all()