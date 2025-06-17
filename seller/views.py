from django.shortcuts import render, redirect
from django.urls import reverse

# Create your views here.
from authentication.models import Profile
from mainapp.models import Product

from .models import ProductListing
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import AddListingForm


class HomeView(ListView):
    model = Product
    template_name = 'seller_products.html'
    context_object_name = 'products'


class ListingDetail(DetailView):
    model = Product
    template_name = 'product_listings.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context =super().get_context_data(**kwargs)
        context['listings'] = ProductListing.objects.filter(product = context['product']).order_by('selling_price')
        # print(self.request.user.username)
        
        context['listing_form'] = AddListingForm()
        
        # print(context)
        return context
    
def addListing(request, product_id):
    this_product = Product.objects.get(id = product_id)
    this_user = request.user
    this_seller = Profile.objects.get(user = this_user)
    if request.method == 'POST':
        price = request.POST.get('selling_price')
        ProductListing.objects.create(product = this_product, seller = this_seller, selling_price = price)
        return redirect(reverse('product_listings', kwargs={'pk' : this_product.pk}))


    