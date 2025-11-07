from django.contrib import admin
from .models import Order, OrderLineItem

class OrderLineItemInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)
    
class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemInline,)
    readonly_fields = ('order_number', 'date', 'stripe_pid', 'original_basket', 'total')
    list_display = ('order_number', 'date', 'full_name', 'total')
    ordering = ('-date',)
    
admin.site.register(Order, OrderAdmin)
