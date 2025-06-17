from django.db import models
from authentication.models import Profile
from django.db.models import Min

# from seller.models import ProductListing

# Create your models here.
class Product(models.Model):
    name= models.CharField(200)
    mrp=models.PositiveIntegerField()
    img=models.ImageField(upload_to='products',null=True)
    desc = models.TextField(max_length=500, null = True)
    seller_profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='product_seller_user')


    def __str__(self):
        return f"product > {self.name}"
    
    @property
    def least_selling_price(self):
        # returns the least selling price for the given product
        selling_price = self.product_listings.aggregate(Min('selling_price'))['selling_price__min']
        

        return selling_price
    
    def listing_id(self):
        # returns the product listing ID of the seller with the least selling price
        listing = self.product_listings.order_by('selling_price').first()
        return listing.id if listing else None


        