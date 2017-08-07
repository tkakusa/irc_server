from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from manager.models import Channel, Post
from manager.serializers import ChannelSerializer, PostSerializer, ChannelIdSerializer, UserModelSerializer
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny


@api_view(['POST'])
@permission_classes((AllowAny, ))
def create_user(request):
    if request.method == 'POST':
        serializer = UserModelSerializer(data=request.data)
        if serializer.is_valid():
            try:
                user = User.objects.create_user(username=request.data['username'],
                                                email=request.data['email'],
                                                password=request.data['password'],
                                                last_name=request.data['last_name'],
                                                first_name=request.data['first_name'])
            except:
                return Response(status=status.HTTP_409_CONFLICT)
            serializer.save(user=user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def channel_list(request, format=None):
    print(request.data)
    if request.method == 'GET':
        channels = Channel.objects.defer("posts")
        serializer = ChannelIdSerializer(channels, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ChannelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST', 'DELETE'])
def channel_detail(request, pk, format=None):
    """
    Retrieve, update or delete a code channel.
    """
    try:
        channel = Channel.objects.get(pk=pk)
    except Channel.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ChannelSerializer(channel)
        print(serializer.data)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ChannelSerializer(channel, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        channel.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def post_list(request, pk, format=None):
    print("Data: ", request.data)
    try:
        channel = Channel.objects.get(pk=pk)
    except Channel.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        posts = Post.objects.filter(channel=channel)
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(channel=channel)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        print("Error: ", serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
