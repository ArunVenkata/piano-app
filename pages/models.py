from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class CustomUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    last_logout = models.DateTimeField(null=True)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        CustomUser.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.customuser.save()


class Record(models.Model):
    audio = models.FileField(upload_to='recordings/', unique=True)
    name = models.CharField(max_length=20)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
