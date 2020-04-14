from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response

from post.serializers import PostSerializer, LikeSerializer, DislikeSerializer
from post.models import Post, Like, Dislike


class PostViewSet(ModelViewSet):

    queryset = Post.objects.all()
    serializer_class = PostSerializer

    @action(detail=True, methods=["PATCH"])
    def like(self, request, pk=None):
        post = self.get_object()
        print(post.likes.users_set)
        self.request.user.username
        serializer = self.get_serializer()
        return Response(serializer.data)

    @action(detail=True, methods=["PATCH"])
    def dislike(self, request, pk=None):
        post = self.get_object()
        self.request.user.username


class LikeViewSet(ModelViewSet):

    queryset = Like.objects.all()
    serializer_class = LikeSerializer


class DislikeViewSet(ModelViewSet):

    queryset = Dislike.objects.all()
    serializer_class = DislikeSerializer
