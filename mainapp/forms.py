from django.forms import ModelForm
from .models import Product

class AddProductForm(ModelForm):
    class Meta:
        model = Product
        exclude = ['seller_profile']