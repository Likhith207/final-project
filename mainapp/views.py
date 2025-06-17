from django.shortcuts import render

from django.views.generic import CreateView,ListView,DeleteView,DetailView,UpdateView
from .models import Product

from django.urls import reverse_lazy

# Create your views here.

def homeView(request):

    products=Product.objects.all()
    context ={
        
        'products':products
    }

    template = 'home.html'

    return render(request, template, context)


class AddProduct(CreateView):
    model=Product
    fields='__all__'
    template_name='add_product.html'
    success_url=reverse_lazy('homepage')

class ProductDetails(DetailView):
    model=Product
    template_name='product_detail.html'
    context_object_name='product'

class DeleteProduct(DeleteView):
    model=Product
    template_name='delete_product.html'
    success_url=reverse_lazy('homepage')

class EditProduct(UpdateView):
    model=Product
    fields='__all__'
    template_name='edit_product.html'
    success_url=reverse_lazy('homepage')


