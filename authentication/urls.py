from django.urls import path

from . import views

urlpatterns=[

    path('login/', views.CustomLoginView.as_view(),name='signin'),
    path('register/', views.UserRegView.as_view(), name = 'signup'),
    path('create_profile/', views.ProfileCreate.as_view(), name = 'create_profile')
]