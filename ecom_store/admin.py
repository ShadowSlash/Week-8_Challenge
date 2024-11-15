from django.contrib import admin 
from ecom_store.models import Orders

# Register your models here.
@admin.register(Orders)
class OrdersAdmin(admin.ModelAdmin):
    list_display = ['customer_name', 'product_name', 'quantity', 'order_date']
    list_filter = ['customer_name', 'product_name', 'order_date']
    show_facets = admin.ShowFacets.ALWAYS