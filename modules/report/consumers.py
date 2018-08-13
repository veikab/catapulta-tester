import json

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer


class ChannelConsumer(WebsocketConsumer):
    def connect(self):
        self.ch_name = self.scope['url_route']['kwargs']['channel_name']
        self.channel_group_name = 'channel_%s' % self.ch_name
        print(self.channel_group_name)

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.channel_group_name,
            self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.channel_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        _id = text_data_json['id']
        name = text_data_json['name']
        file = text_data_json['file']
        create_at = text_data_json['create_at']

        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.channel_group_name,
            {
                'id': _id,
                'type': 'chat_message',
                'name': name,
                'file': file,
                'create_at': create_at
            }
        )

    # Receive message from room group
    def chat_message(self, event):
        _id = event['id']
        name = event['name']
        file = event['file']
        create_at = event['create_at']

        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'id': _id,
            'name': name,
            'file': file,
            'create_at': create_at
        }))