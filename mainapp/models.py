from django.db import models

# Create your models here.
class Product(models.Model):
    name= models.CharField(200)
    mrp=models.PositiveIntegerField()
    img=models.ImageField(upload_to='products',null=True)


    def __str__(self):
        return f"product > {self.name}"
