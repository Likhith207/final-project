from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view() , name = 'seller_home'),
    path('product_details/<int:pk>', views.ListingDetail.as_view(), name = 'product_listings'),
    path('listing/add/<int:product_id>', views.addListing, name = 'add_listing')
]