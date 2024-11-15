from django.utils import timezone 
from django.db import models

# Create your models here.

class Store(models.Model): 
    customer_name = models.CharField(max_length=100)
    product_name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    order_date = models.DateField(default=timezone.now)

    def __str__(self): 
        return f"{self.customer_name} has ordered {self.product_name} // Quantity: {self.quantity} // On the {self.order_date}"