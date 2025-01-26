from django.contrib import admin
from .models import Category, Product, Order, Payment


# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'price', 'stock', 'category']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'date', 'status']


class PaymentAdmin(admin.ModelAdmin):
    list_display = ['order', 'user', 'date', 'total_sum', 'payment_method']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Payment, PaymentAdmin)
