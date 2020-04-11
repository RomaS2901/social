from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet

from post.serializers import PostSerializer, LikeSerializer, DislikeSerializer
from post.models import Post, Like, Dislike


class PostViewSet(ModelViewSet):

    queryset = Post.objects.all()
    serializer_class = PostSerializer


class LikeViewSet(ModelViewSet):

    queryset = Like.objects.all()
    serializer_class = LikeSerializer


class DislikeViewSet(ModelViewSet):

    queryset = Dislike.objects.all()
    serializer_class = DislikeSerializer
