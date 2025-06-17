from django.urls import path

from . import views

urlpatterns=[
    path('', views.homeView, name='homepage'),
    path('product/<int:pk>', views.ProductDetails.as_view(), name = 'product-detail'),
    path('product/add', views.AddProduct.as_view(), name = 'add_product'),
    path('product/edit/<int:pk>', views.EditProduct.as_view(),name='edit_product'),
    path('product/del/<int:pk>',views.DeleteProduct.as_view(),name='delete_product')
]