from django.urls import path
from .views import order_list, order_create, order_edit, order_delete

urlpatterns = [
    path('', order_list, name='order_list'),
    path('new/', order_create, name='order_create'),
    path('<int:pk>/edit/', order_edit, name='order_edit'),
    path('<int:pk>/delete/', order_delete, name='order_delete'),
]
