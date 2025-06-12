from django.urls import path

from . import views

urlpatterns=[
    path('', views.homeView, name='homepage'),
     path('product/<int:pk>', views.ProductDetails.as_view(), name = 'product-detail'),
]