from django.shortcuts import render

from django.views.generic import CreateView,ListView,DeleteView,DetailView,UpdateView
from .models import Product
from .forms import AddProductForm
from seller.models import ProductListing
from authentication.models import Profile
from django.urls import reverse_lazy
from django.shortcuts import redirect

# Create your views here.

def homeView(request):
    try: 
        profile = Profile.objects.get(user = request.user)
        # print("Yeay")
        if profile.user_role == 'seller':
            # print("seller")
            return redirect('seller_home')
        else:
            pass
            
    except:
        pass
        # print("no")
    products=Product.objects.all()
    context ={
        
        'products':products
    }

    template = 'home.html'

    return render(request, template, context)


class AddProduct(CreateView):
    model=Product
    # fields='__all__'
    form_class = AddProductForm
    template_name='add_product.html'
    success_url=reverse_lazy('homepage')
    
    def form_valid(self, form):
        form.instance.seller_profile = self.request.user.user_profile
        return super().form_valid(form)
    
    

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


