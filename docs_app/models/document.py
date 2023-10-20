from django.db import models
    
class Document(models.Model):
    name = models.CharField()
    date_created = models.DateTimeField()
    date_modified = models.DateTimeField()
    creator = models.BigIntegerField()
    tag_id = models.BigIntegerField()
    viewer_group = models.BigIntegerField()
    editor_group = models.BigIntegerField()
    moderator_group = models.BigIntegerField()