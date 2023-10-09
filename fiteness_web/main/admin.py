from django.contrib import admin
from .models import Service

@admin.register(Service)
class ServiceModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name','service_image','duration','price','created_at','updated_at']