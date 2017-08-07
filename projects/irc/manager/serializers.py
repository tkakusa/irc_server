from rest_framework import serializers
from manager.models import Channel, Post, UserModel

class UserModelSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username')
    email = serializers.CharField(source='user.email')
    password = serializers.CharField(source='user.password')
    first_name = serializers.CharField(source='user.first_name')
    last_name = serializers.CharField(source='user.last_name')

    class Meta:
        model = UserModel
        fields = ('id', 'username', 'email', 'password', 'first_name', 'last_name', 'address', 'state', 'zip')

    def update(self, instance, validated_data):
        instance.user.email = attrs.get('user.email', instance.user.email)
        instance.user.password = attrs.get('user.password', instance.user.password)
        instance.user.first_name = attrs.get('user.first_name', instance.user.first_name)
        instance.user.last_name = attrs.get('user.last_name', instance.user.last_name)
        instance.address = attrs.get('address', instance.address)
        instance.state = attrs.get('state', instance.state)
        instance.zip = attrs.get('zip', instance.zip)
        instance.save()
        return instance

    def create(self, validated_data):
        return UserModel.objects.create(**validated_data)

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'created', 'message')
        
class ChannelSerializer(serializers.ModelSerializer):
    posts = PostSerializer(many=True, read_only=True)
    class Meta:
        model = Channel
        fields = ('id', 'name', 'description', 'posts', 'tag')

class ChannelIdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Channel
        fields = ('id', 'name', 'description', 'tag')
