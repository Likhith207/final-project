from django.shortcuts import render

from django.views.generic import CreateView,ListView,DeleteView,DetailView,UpdateView
from .models import Product

# Create your views here.

def homeView(request):

    products=Product.objects.all()
    context ={
        
        'products':products
    }

    template = 'home.html'

    return render(request, template, context)

class ProductDetails(DetailView):
    model=Product
    template='product_detail.html'
    context_object_name='product'


