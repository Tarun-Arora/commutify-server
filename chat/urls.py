from django.urls import path

from .views import RequestRoomAccessView
from . import views

urlpatterns = [
    path('room_access/', RequestRoomAccessView.as_view()),
    path('<str:room_name>/', views.room, name='room'),
    path('', views.index, name='index'),
]
