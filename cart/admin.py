from django.contrib import admin
from .models import CartItem, OrderItem


class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_at', 'is_complete', 'menu', 'size', 'style', 'additional', 'is_special', 'price', 'user_id')
    list_editable = ['is_complete']


admin.site.register(CartItem)
admin.site.register(OrderItem, OrderItemAdmin)
