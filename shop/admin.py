from django.contrib import admin
from .models import Product, Order

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'available', 'created_at')
    list_filter = ('available', 'created_at')
    search_fields = ('name', 'description')
    list_editable = ('price', 'available')
    prepopulated_fields = {'slug': ('name',)}

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'completed', 'created_at')
    list_filter = ('completed', 'created_at')
    search_fields = ('user__username', 'products__name')
    filter_horizontal = ('products',)
    readonly_fields = ('created_at',)

admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)