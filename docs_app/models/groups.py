from django.db import models
    
class Groups(models.Model):
    name = models.CharField()
    description = models.CharField()
    