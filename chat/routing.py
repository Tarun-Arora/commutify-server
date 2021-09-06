from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/chat/(?P<room_name>[^/]+)/(?P<username>[^/]+)/$', consumers.ChatConsumer.as_asgi()),
    re_path(r'ws/message/$', consumers.MessageUpdate.as_asgi()),
]