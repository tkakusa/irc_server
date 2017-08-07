from manager.models import Channel, Post
from manager.serializers import ChannelSerializer, PostSerializer, ChannelIdSerializer

channels = Channel.objects.defer("posts", "name")
channel = channels[0]
#Post.objects.create(channel=channel, message="test message")
serializer = ChannelIdSerializer(channel)
print(serializer.data)

