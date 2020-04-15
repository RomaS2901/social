from django.db.utils import IntegrityError

from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

from post.serializers import PostSerializer, LikeSerializer, DislikeSerializer
from post.models import Post, Like, Dislike


class PostViewSet(ModelViewSet):

    queryset = Post.objects.all()
    serializer_class = PostSerializer

    @action(detail=True, methods=["POST"])
    def like(self, request, pk=None):
        post = self.get_object()
        # remove dislike, if user disliked that post before
        if post.dislikes.filter(user=request.user).exists():
            post.dislikes.get(user=request.user).delete()
        try:
            post.likes.create(user=request.user)
        except IntegrityError:
            # means already liked by this user
            pass
        serializer = self.get_serializer(post)
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    @action(detail=True, methods=["POST"])
    def dislike(self, request, pk=None):
        post = self.get_object()
        if post.likes.filter(user=request.user).exists():
            post.likes.get(user=request.user).delete()
        try:
            post.dislikes.create(user=request.user)
        except IntegrityError:
            pass
        serializer = self.get_serializer(post)
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)


class LikeViewSet(ReadOnlyModelViewSet):

    queryset = Like.objects.all()
    serializer_class = LikeSerializer


class DislikeViewSet(ReadOnlyModelViewSet):

    queryset = Dislike.objects.all()
    serializer_class = DislikeSerializer
