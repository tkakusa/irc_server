from manager.models import Channel, Post
from manager.serializers import ChannelSerializer, PostSerializer

channel = Channel.objects.all()
channel = channel[0]
serializer = ChannelSerializer(instance=channel)
print(serializer.data)
