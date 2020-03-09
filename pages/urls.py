from django.urls import path
from django.views.generic import TemplateView
from pages import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('signup', views.SignupView.as_view(), name='signup'),
    path('logout/', views.last_logout, name='logout'),
    path('app', login_required(TemplateView.as_view(template_name='piano_layout.html')), name='piano'),
    path("", views.HomeView.as_view(), name='home'),
    path("user-update/<int:pk>", views.UserUpdateView.as_view(), name='user-update'),
    path('recordings', views.RecordingList.as_view(), name='recordings'),
    path('download/<int:pk>', views.DownloadRecordings.as_view(), name='download'),
    path('delete/<int:pk>', views.DeleteRecordings.as_view(), name='delete'),
    path("api/record", views.RecordAPI.as_view(), name='record'),
    path('download', views.download, name='download'),
]
