from django.contrib import admin
from .models import cart


# Register your models here.
@admin.register(cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['user','products','quantity']
