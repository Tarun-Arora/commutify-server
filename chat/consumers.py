import json

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from rest_framework.authtoken.models import Token

from authentication.models import msg, UserInfo, Chat


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        token = self.scope['url_route']['kwargs']['token']
        self.room_group_name = 'chat_%s' % self.room_name

        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        try:
            user = Token.objects.get(key=token).user
        except:
            return
        try:
            chat = Chat.objects.get(title=self.room_name)
        except:
            return
        if user in chat.users.all():
            self.accept()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        token = self.scope['url_route']['kwargs']['token']
        chat_requested = self.room_name
        chat_room = Chat.objects.get(title=chat_requested)
        try:
            sender = Token.objects.get(key=token).user
        except:
            return
        q = msg.objects.create(sender_id=sender, chat_room=chat_room, message=message, dttime=timezone.now())
        q.save()
        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'sender': str(sender)
            }
        )

    # Receive message from room group
    def chat_message(self, event):
        message = event['message']
        dttime = timezone.now()
        sender = event['sender']

        # Send message to WebSocket
        self.send(text_data=json.dumps({'message': message,'dttime': str(dttime),'sender': str(sender)}))


class MessageUpdate(WebsocketConsumer):
    def connect(self):
        self.room_name = 'update'
        self.room_group_name = 'chat_%s' % self.room_name
        token = self.scope['url_route']['kwargs']['token']
        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        try:
            user = Token.objects.get(key=token).user
        except:
            return
        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        room = text_data_json['room']
        try:
            chat = Chat.objects.get(title=room)
        except:
            return
        token = self.scope['url_route']['kwargs']['token']
        try:
            user = Token.objects.get(key=token).user
        except:
            return
        if(user not in chat.users.all()):
            return
        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'room': room,
                'message': message
            }
        )

    # Receive message from room group
    def chat_message(self, event):
        message = event['message']
        room = event['room']

        chat = Chat.objects.get(title=room)
        token = self.scope['url_route']['kwargs']['token']
        try:
            user = Token.objects.get(key=token).user
        except:
            return
        if user in chat.users.all():
            self.send(text_data=json.dumps({
                'message': message,
                'room': room
            }))
        # Send message to WebSocket
