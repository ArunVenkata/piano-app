from django.urls import path
from pages import views

urlpatterns = [
    path('signup', views.SignupView.as_view(), name='signup'),
    path('', views.HomeView.as_view(), name='home'),
]
