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
        # if used left dislike and changed his mind
        if post.dislikes.users.filter(username=self.request.user.username).exists():
            post.dislikes.users.remove(self.request.user)
        post.likes.users.add(self.request.user)
        serializer = self.get_serializer(post)
        return Response(serializer.data)

    @action(detail=True, methods=["PATCH"])
    def dislike(self, request, pk=None):
        post = self.get_object()
        if post.likes.users.filter(username=self.request.user.username).exists():
            post.likes.users.remove(self.request.user)
        post.dislikes.users.add(self.request.user)
        serializer = self.get_serializer(post)
        return Response(serializer.data)


class LikeViewSet(ModelViewSet):

    queryset = Like.objects.all()
    serializer_class = LikeSerializer


class DislikeViewSet(ModelViewSet):

    queryset = Dislike.objects.all()
    serializer_class = DislikeSerializer
