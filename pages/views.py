from django.views.generic import CreateView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from pages.forms import CustomUserCreationForm


class SignupView(CreateView):
    form_class = CustomUserCreationForm
    template_name = "registration/signup.html"
    success_url = "/"


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'piano_layout.html'
