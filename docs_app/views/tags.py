from rest_framework import viewsets
from docs_app.serializers import TagSerializer
from docs_app.models import Tags

class TagViewSet(viewsets.ModelViewSet):
    serializer_class = TagSerializer
    queryset = Tags.objects.all()