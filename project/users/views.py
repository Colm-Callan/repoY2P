from django.urls import reverse_lazy
from .forms import CustomUserCreationForm
from django.views.generic import TemplateView, CreateView, DetailView
from .models import CustomUser
from  django.shortcuts import render
class HomePageView(TemplateView):
    template_name = 'home.html'

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
    
class UserProfileView(DetailView):
    model = CustomUser
    template_name = 'registration/user_profile.html'

    def post(self, request, *args, **kwargs):
        object_instance = self.get_object()
        object_instance.is_loyal = True
        object_instance.save()
        success_message = "You have successfully signed up for the loyal customer."
        return render(request, self.template_name, {'object': object_instance, 'success_message': success_message})



