import json

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from rest_framework.authtoken.models import Token

from authentication.models import msg, UserInfo, Chat, Group


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
                'message': message,
                'sender': str(user.username)
            }
        )

    # Receive message from room group
    def chat_message(self, event):
        message = event['message']
        room = event['room']
        sender = event['sender']

        chat = Chat.objects.get(title=room)
        token = self.scope['url_route']['kwargs']['token']
        try:
            user = Token.objects.get(key=token).user
        except:
            return
        if user in chat.users.all():
            self.send(text_data=json.dumps({
                'message': message,
                'room': room,
                'sender': sender,
            }))
        # Send message to WebSocket






class RequestsSocket(WebsocketConsumer):
    def connect(self):
        self.room_name = 'requests'
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
        type_request = text_data_json['type']
        username = text_data_json['username']
        token = self.scope['url_route']['kwargs']['token']
        print(text_data)
        try:
            user = Token.objects.get(key=token).user
        except:
            return
        # Send message to room group
        if type_request == 0:
            async_to_sync(self.channel_layer.group_send)(
                self.room_group_name,
                {
                    'type': 'chat_message',
                    'type_request': type_request,
                    'username': username,
                    'sender': str(user.username)
                }
            )
        else:
            id = text_data_json['id']
            async_to_sync(self.channel_layer.group_send)(
                self.room_group_name,
                {
                    'type': 'chat_message',
                    'type_request': type_request,
                    'username': username,
                    'sender': str(user.username),
                    'id': id
                }
            )

    # Receive message from room group
    def chat_message(self, event):
        type_request = event['type_request']
        username = event['username']
        sender = event['sender']

        token = self.scope['url_route']['kwargs']['token']
        try:
            user = Token.objects.get(key=token).user
        except:
            return
        if type_request == 0:
            if str(user.username) == username:
                fr = UserInfo.objects.get(username=sender)
                self.send(text_data=json.dumps({
                    'username': fr.username,
                    'first_name': fr.first_name,
                    'last_name': fr.last_name,
                    'type': 0
                }))
        else:
            if str(user.username) == username:
                id = event['id']
                grp = Group.objects.get(id=id)
                self.send(text_data=json.dumps({
                    'id': grp.id,
                    'name': grp.name,
                    'type': 1,
                    'description': grp.description
                }))


        # Send message to WebSocket