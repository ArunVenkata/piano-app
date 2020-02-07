from django.urls import path
from django.views.generic import TemplateView
from pages import views

urlpatterns = [
    path('signup', views.SignupView.as_view(), name='signup'),
    path('app', views.HomeView.as_view(), name='home'),
    path("", TemplateView.as_view(template_name="index.html")),
    path("api/record", views.RecordAPI.as_view(), name='record'),
]
