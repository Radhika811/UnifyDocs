from rest_framework import viewsets
from docs_app.serializers import DocumentSerializer
from docs_app.models import Document

class DocumentViewSet(viewsets.ModelViewSet):
    serializer_class = DocumentSerializer
    queryset = Document.objects.all()