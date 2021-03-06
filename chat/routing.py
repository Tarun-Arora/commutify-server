from django.urls import re_path

import django
django.setup()
from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/message/(?P<token>[^/]+)/$', consumers.MessageUpdate.as_asgi()),
    re_path(r'ws/requests/(?P<token>[^/]+)/$', consumers.RequestsSocket.as_asgi()),
]