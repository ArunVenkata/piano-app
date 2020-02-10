from django.views.generic import CreateView, View, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from pages.forms import CustomUserCreationForm
from pages.util import render_audio
from pages.models import Record
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated


class SignupView(CreateView):
    form_class = CustomUserCreationForm
    template_name = "registration/signup.html"
    success_url = "/app"


class HomeView(View):

    @staticmethod
    def get(request):
        if request.user.is_authenticated:
            return redirect('piano')
        else:
            return render(request, 'index.html')


class PianoView(LoginRequiredMixin, TemplateView):
    template_name = 'piano_layout.html'


class RecordAPI(APIView):
    permission_classes = (IsAuthenticated,)

    @staticmethod
    def post(request):
        path = render_audio(request.data)
        record = Record(audio=path, name=request.data['FileName'], user=request.user)
        record.save()
        return JsonResponse({
            'url': path
        })
