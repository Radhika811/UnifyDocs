from django.contrib import admin
from .models import *

admin.site.register(User)
admin.site.register(Tags)
admin.site.register(Groups)
admin.site.register(Document)