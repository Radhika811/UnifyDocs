# from rest_framework import viewsets
# from docs_app.serializers import DocumentSerializer
# from docs_app.models import Document

# class DocumentViewSet(viewsets.ModelViewSet):
#     serializer_class = DocumentSerializer
#     queryset = Document.objects.all()

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets
from django.views.decorators.csrf import csrf_exempt
from docs_app.serializers import DocumentSerializer
from docs_app.models import Document

@csrf_exempt  # Disable CSRF protection for this view
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def document_list(request):
    if request.method == 'GET':
        documents = Document.objects.all()
        serializer = DocumentSerializer(documents, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = DocumentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

@csrf_exempt  # Disable CSRF protection for this view
@api_view(['GET', 'PUT', 'DELETE', 'POST'])
def document_detail(request, pk):
    try:
        document = Document.objects.get(pk=pk)
    except Document.DoesNotExist:
        return Response(status=404)

    if request.method == 'GET':
        serializer = DocumentSerializer(document)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = DocumentSerializer(document, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    elif request.method == 'DELETE':
        document.delete()
        return Response(status=204)
    elif request.method == 'POST':
        serializer = DocumentSerializer(document)
        return Response(serializer.data)
