from django.db import models
from .document import Document
    
class Tags(models.Model):
    number = models.IntegerField()
    name = models.CharField()
    description = models.CharField()
    doc_id = models.ForeignKey(Document, on_delete=models.CASCADE, related_name="document")