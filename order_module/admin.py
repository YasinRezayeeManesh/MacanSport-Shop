from django.contrib import admin

from order_module.models import Order, OrderDetail


# Register your models here.


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'is_paid', 'is_close', 'date_paid']


@admin.register(OrderDetail)
class OrderDetailAdmin(admin.ModelAdmin):
    list_display = ['order', 'final_price']
