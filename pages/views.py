from django.views.generic import CreateView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from pages.forms import CustomUserCreationForm
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from pydub import AudioSegment


class SignupView(CreateView):
    form_class = CustomUserCreationForm
    template_name = "registration/signup.html"
    success_url = "/app"


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'piano_layout.html'


class RecordAPI(APIView):

    permission_classes = (IsAuthenticated,)

    def post(self, request):
        data = request.data
        base = AudioSegment.silent(duration=data['TotalTime'])
        for i in data["Keys"].keys():
            keyAudio = AudioSegment.from_wav('static/sounds/' + data['Keys'][i] + '.wav')
            base = base.overlay(keyAudio, position=int(i))
        base.export('media/new.wav', format='wav')
        return JsonResponse({
            'status': 'done'
        })
