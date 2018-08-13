from django.conf.urls import url

from . import consumers

websocket_urlpatterns = [
    url(r'^ws/channel/(?P<channel_name>[^/]+)/$', consumers.ChannelConsumer),
]