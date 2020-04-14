from django.contrib.auth import get_user_model

from rest_framework import serializers

from post.models import Post, Like, Dislike


class PostSerializer(serializers.ModelSerializer):

    likes = serializers.IntegerField(source="get_likes")
    dislikes = serializers.IntegerField(source="get_dislikes")

    class Meta:
        model = Post
        fields = "__all__"


class LikeSerializer(serializers.ModelSerializer):

    # Have ability to create likes and dislikes using username field instead of raw pk
    #   as username field is unqiue as well
    users = serializers.SlugRelatedField(
        slug_field="username", queryset=get_user_model().objects.all(), many=True
    )

    class Meta:
        model = Like
        fields = "__all__"


class DislikeSerializer(serializers.ModelSerializer):

    users = serializers.SlugRelatedField(
        slug_field="username", queryset=get_user_model().objects.all(), many=True
    )

    class Meta:
        model = Dislike
        fields = "__all__"
