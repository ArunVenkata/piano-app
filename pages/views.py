from django.views.generic import CreateView, View, ListView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render, HttpResponse
from pages.forms import CustomUserCreationForm
from pages.util import render_audio
from django.utils.encoding import smart_str
from pages.models import Record
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User


class SignupView(CreateView):
    form_class = CustomUserCreationForm
    template_name = "registration/signup.html"
    success_url = "/logout"


class HomeView(View):
    @staticmethod
    def get(request):
        if request.user.is_authenticated:
            return redirect('piano')
        else:
            return render(request, 'index.html')

def download(request):
    file = open('media/test.mp3', 'rb').read()
    response = HttpResponse(file)
    response['Content-Disposition'] = 'attachment; filename=test.mp3'
    return response


class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = CustomUserCreationForm
    template_name = 'registration/update.html'


class RecordingList(LoginRequiredMixin, ListView):
    template_name = 'recordings.html'
    context_object_name = 'recordings'

    def get_queryset(self):
        return Record.objects.filter(user=self.request.user)


class DownloadRecordings(LoginRequiredMixin, View):
    @staticmethod
    def get(request, pk):
        recording = Record.objects.filter(pk=pk).first()
        if request.user == recording.user:
            file = open(recording.audio.url[1:], 'rb')
            response = HttpResponse(file, content_type='audio/mpeg')
            response['Content-Disposition'] = 'attachment; filename=%s' % smart_str(recording.name + '.wav')
            return response
        else:
            return HttpResponse("Not Authorized")


class RecordAPI(APIView):
    permission_classes = (IsAuthenticated,)

    @staticmethod
    def post(request):
        path = render_audio(request.data)
        record = Record(audio=path, name=request.data['FileName'], user=request.user)
        record.save()
        return JsonResponse({
            'status': path
        })
