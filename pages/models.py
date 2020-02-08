from django.db import models
from django.contrib.auth.models import User


class Record(models.Model):
    audio = models.FileField(upload_to='recordings/', unique=True)
    name = models.CharField(max_length=20)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
