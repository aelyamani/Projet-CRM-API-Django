from django.contrib import admin
from .models import Client, Document

# Register your models here.
admin.site.register(Document)
admin.site.register(Client)
