from django.db import models

class User(models.Model):
    name = models.CharField()
    year = models.IntegerField()
    enrollment = models.BigIntegerField()