from django.contrib import admin
from .models import Service, ServiceRequest

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'hourly_rate', 'available', 'created_at')
    list_filter = ('available', 'created_at')
    search_fields = ('title', 'description')
    list_editable = ('hourly_rate', 'available')
    prepopulated_fields = {'slug': ('title',)}

@admin.register(ServiceRequest)
class ServiceRequestAdmin(admin.ModelAdmin):
    list_display = ('service', 'user', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('service__title', 'user__username')
    readonly_fields = ('created_at',)