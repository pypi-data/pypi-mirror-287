from django.contrib import admin
from artd_service.models import Service

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = (
        'id', 
        'name', 
        'description', 
        'slug', 
        'created_at', 
        'updated_at', 
        'status',
    )