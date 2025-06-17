from django.forms import ModelForm
from .models import ProductListing

class AddListingForm(ModelForm):
    class Meta:
        model = ProductListing
        exclude = ['seller', 'product']