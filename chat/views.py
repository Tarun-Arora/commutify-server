from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponseNotFound
from django.shortcuts import render, redirect
from rest_framework import status
from rest_framework.response import Response

from authentication.models import UserInfo, Group, Chat


@login_required
def index(request):
    print(request.user)
    return render(request, 'chat/index.html')


@login_required
def room(request, room_name):
    try:
        chat_requested = room_name.split('-')
    except:
        return HttpResponseNotFound('<h1>Page not found</h1>')
    if len(chat_requested) == 3:
        try:
            verified = Chat.objects.get(title=room_name)
        except:
            return HttpResponseNotFound('<h1>Page not found</h1>')
        return render(request, 'chat/room.html', {
            'room_name': room_name
        })
    if len(chat_requested) == 2:
        try:
            grp = Group.objects.get(id=chat_requested[1])
            verified = Chat.objects.get(title=room_name)
        except:
            return HttpResponseNotFound('<h1>Page not found</h1>')
        if request.user not in grp.members.all() and request.user not in grp.admins.all():
            return HttpResponseNotFound('<h1>Page not found</h1>')
        return render(request, 'chat/room.html', {
            'room_name': room_name
        })




