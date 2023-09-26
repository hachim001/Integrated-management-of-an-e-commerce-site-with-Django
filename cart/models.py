from django.db import models
from django.contrib.auth.models import User
from product.models import Product

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    size = models.CharField(max_length=50, null=True)
    quantity = models.IntegerField(default=1)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    

    def __str__(self):
        return f"{self.product.title} - Size: {self.size} - Quantity: {self.quantity}"
    
