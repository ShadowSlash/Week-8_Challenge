from django.urls import path
from .views import order_list, order_create, order_edit, order_delete, home

app_name = 'ecom_store'

urlpatterns = [
    path('', home, name='homepage'),
    path('orders', order_list, name='order_list'),
    path('order/create/', order_create, name='order_create'),
    path('order/<int:pk>/edit/', order_edit, name='order_edit'),
    path('order/<int:pk>/delete/', order_delete, name='order_delete'),
]
