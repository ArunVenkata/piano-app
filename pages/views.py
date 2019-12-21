from django.shortcuts import render
from django.http import HttpResponse as Response

# Create your views here.

def home_view(request, *args, **kwargs):
    return render(request, "piano_layout.html")