from django.contrib import admin
from .models import OrderItems,Order

# Register your models here.
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['user','total_price','created_at']



@admin.register(OrderItems)
class OrderItemsAdmin(admin.ModelAdmin):
    list_display = ['order','product','quantity']
