from django.db import models
    
class Groups(models.Model):
    name = models.CharField()
    user_id = models.IntegerField()
    