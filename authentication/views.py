from django.shortcuts import render
from django.urls import reverse

from django.contrib.auth.models import User
from .models import Profile
from django.contrib.auth.views import LoginView

from django.urls import reverse_lazy

from django.views.generic import CreateView, DetailView, UpdateView
from .forms import CustomLoginForm, CustomRegForm, ProfileCreationForm
# Create your views here.

class CustomLoginView(LoginView):
    template_name="signin.html"
    form_class = CustomLoginForm

    def get_success_url(self):
        if Profile.objects.filter(user = self.request.user).exists():
            return super().get_success_url()
        else:
            return reverse_lazy('create_profile')

class UserRegView(CreateView):
    model=User
    form_class=CustomRegForm
    template_name='signup.html'
    success_url=reverse_lazy('signin')

    


class ProfileCreate(CreateView):
    model = Profile
    form_class = ProfileCreationForm
    template_name = 'create_profile.html'
    success_url = '/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ProfileView(DetailView):
    model = Profile
    template_name = 'profile.html'
    context_object_name = 'user_profile'


class ProfileEditView(UpdateView):
    model = Profile
    template_name = 'edit_profile.html'
    fields = ['first_name', 'last_name', 'email', 'profile_photo', 'phone_number', 'address']
    
    def get_success_url(self):
        return reverse('profile', kwargs={'pk':self.request.user.user_profile.id})

    def get_object(self, queryset=None):
        return self.request.user.user_profile