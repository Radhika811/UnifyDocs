from django.db import models
from .user import User
from .tags import Tags
from .groups import Groups
from ckeditor.fields import RichTextField
    
class Document(models.Model):
    number = models.IntegerField()
    name = models.CharField()
    content = RichTextField()
    date_created = models.DateTimeField()
    date_modified = models.DateTimeField()
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name="creator")
    viewer_group = models.ForeignKey(Groups, on_delete=models.CASCADE, related_name="viewer_group")
    editor_group = models.ForeignKey(Groups, on_delete=models.CASCADE, related_name="editor_group")
    moderator_group = models.ForeignKey(Groups, on_delete=models.CASCADE, related_name="moderator_group")