from django.urls import path
from django.views.generic import TemplateView
from pages import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('signup', views.SignupView.as_view(), name='signup'),
    path('app', login_required(TemplateView.as_view(template_name='piano_layout.html')), name='piano'),
    path("", views.HomeView.as_view(), name='home'),
    path('recordings', views.RecordingList.as_view(), name='recordings'),
    path("api/record", views.RecordAPI.as_view(), name='record'),
]
