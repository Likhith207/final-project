from django.urls import path

from . import views

urlpatterns=[

    path('login/', views.CustomLoginView.as_view(),name='signin'),
    path('register/', views.UserRegView.as_view(), name = 'signup'),
    path('create_profile/', views.ProfileCreate.as_view(), name = 'create_profile'),
    path('profile/<int:pk>', views.ProfileView.as_view(), name = 'profile'),
    path('profile/edit/', views.ProfileEditView.as_view(), name='edit_profile'),

]