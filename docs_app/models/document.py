from django.db import models
from .user import User
from .groups import Groups
    
class Document(models.Model):
    number = models.IntegerField()
    name = models.CharField()
    description = models.TextField()
    content = models.TextField(null = True, blank = True)
    date_created = models.DateTimeField()
    date_modified = models.DateTimeField()
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name="creator")