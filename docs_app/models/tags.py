from django.db import models
    
class Tags(models.Model):
    name = models.CharField()
    doc_id = models.BigIntegerField()