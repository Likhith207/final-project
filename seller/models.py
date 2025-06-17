from django.db import models
from django.contrib.auth.models import User
from authentication.models import Profile

from mainapp.models import Product
# Create your models here.


class ProductListing(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_listings')
    seller = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='product_listing_seller')
    selling_price = models.PositiveIntegerField(default=0)


    def __str__(self):
        return f"{self.product.name} sold by {self.seller.first_name.capitalize()} {self.seller.last_name}"
    