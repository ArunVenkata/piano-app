from django.urls import path
from django.views.generic import TemplateView
from pages import views

urlpatterns = [
    path('signup', views.SignupView.as_view(), name='signup'),
    path('app', views.PianoView.as_view(), name='piano'),
    path("", views.HomeView.as_view(), name='home'),
    path("api/record", views.RecordAPI.as_view(), name='record'),
]
