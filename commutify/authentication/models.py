from django.contrib import admin
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.deletion import CASCADE, SET_NULL
from django.db.models.fields import EmailField


# class msg(models.Model):
#     sender_id = models.ForeignKey('UserInfo', on_delete=CASCADE)
#     dttime = models.DateTimeField(auto_now=True)
#     message = models.CharField(max_length=1024)

# class Chat(models.Model):
#     msgs = models.ManyToManyField(msg, related_name='listmsgs', blank=True)

class UserInfo(AbstractUser):
    # groups = models.ManyToManyField('Group', related_name='groups', blank=True)
    status = models.CharField(max_length=256, default='Start', blank=True)
    dob = models.DateField(null=True)
    # friends = models.ManyToManyField('Friend', blank=True)
    friend_requests = models.ManyToManyField('UserInfo', blank=True, default=None)
    # group_requests = models.ManyToManyField('Group', blank=True, default=None)
    verify_pin = models.IntegerField(null=True)
    is_verified = models.BooleanField(default=False)

# class Friend(models.Model):
#     user = models.ForeignKey(UserInfo, on_delete=CASCADE)
#     chats = models.ForeignKey(Chat, on_delete=CASCADE)

# class Group(models.Model):
#     members = models.ManyToManyField(UserInfo, related_name='members', blank=True)
#     admins = models.ManyToManyField(UserInfo, related_name='admins')
#     description = models.CharField(max_length=256, default='')
#     name = models.CharField(max_length=32, default='')
#     groupDP = models.ImageField(null=True, blank=True)
#     chats = models.ForeignKey(Chat, on_delete=CASCADE, blank=True, null=True)

class ForgotPwdRequest(models.Model):
    email = models.EmailField()
    sttime = models.DateTimeField(auto_now=True)
    otp = models.IntegerField()