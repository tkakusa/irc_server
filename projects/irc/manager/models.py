from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

class UserModel(models.Model):
    user = models.OneToOneField(User)
    address = models.CharField(max_length=100, blank=True, default='')
    state = models.CharField(max_length=50, blank=True, default='')
    zip = models.IntegerField(default=0)

class Channel(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    tag = models.CharField(max_length=10)

    class Meta:
        ordering = ('name',)

class Post(models.Model):
    channel = models.ForeignKey(Channel, related_name='posts', on_delete=models.CASCADE, default=0)
    created = models.DateTimeField(auto_now_add=True)
    message = models.CharField(max_length=400)

    class Meta:
        ordering = ('created',)
