from django.db import models

# importing the User model
from django.contrib.auth.models import User 
# import Product model from mainapp
from mainapp.models import Product

from seller.models import ProductListing


# Create your models here.
class CartItem(models.Model):
    product_listing = models.ForeignKey(ProductListing, on_delete= models.CASCADE)
    # Foreign key(product_id) references mainapp_product(id) on delete cascade

    user    = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default= 0)
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username.capitalize()} added {self.product_listing.product.name} to cart!!!"
    
    def sub_total(self):
        return self.quantity * self.product_listing.selling_price 