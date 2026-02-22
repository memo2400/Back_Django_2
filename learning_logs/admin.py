from django.contrib import admin

# Register your models here.
from .models import Topic, Entry

admin.site.register(Topic) #manejamos como admin site el modelo
admin.site.register(Entry)
