from django.db import models
from django.contrib.auth.models import AbstractUser
    
class User(AbstractUser):
    user_role = [
        ('a', 'admin'),
        ('n', 'normal_user')
    ]
    
    enrollment = models.BigIntegerField(unique = True, null=True)
    email = models.EmailField(null = True)
    phone_no = models.CharField(max_length=12, null=True)
    gender = models.CharField(max_length=60)
    name = models.CharField(max_length=60)
    year = models.IntegerField(null = True)  
    role = models.CharField(max_length=1, choices=user_role, default='n')
    
    class Meta:
        unique_together=('name','enrollment')
    