from django.db import models
from .user import User
    
class Groups(models.Model):
    number = models.IntegerField()
    name = models.CharField()
    description = models.CharField()
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="owner")
    