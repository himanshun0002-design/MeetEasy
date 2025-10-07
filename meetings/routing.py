from django.urls import re_path
from ..meeteasy import consumers

websocket_urlpatterns = [
    re_path(r'ws/room/(?P<room_name>[^/]+)/$', consumers.RoomConsumer.as_asgi()),
]
