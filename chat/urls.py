from django.urls import path

from .views import RequestRoomAccessView

urlpatterns = [
    path('room_access/', RequestRoomAccessView.as_view()),
]
