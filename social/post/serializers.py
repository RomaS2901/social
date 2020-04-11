from rest_framework.serializers import ModelSerializer

from post.models import Post, Like, Dislike


class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"


class LikeSerializer(ModelSerializer):
    class Meta:
        model = Like
        fields = "__all__"


class DislikeSerializer(ModelSerializer):
    class Meta:
        model = Dislike
        fields = "__all__"
