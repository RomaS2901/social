from django.contrib.auth import get_user_model

from rest_framework import serializers

from post.models import Post, Like, Dislike


class PostSerializer(serializers.ModelSerializer):

    likes = serializers.IntegerField(source="get_likes", read_only=True)
    dislikes = serializers.IntegerField(source="get_dislikes", read_only=True)

    class Meta:
        model = Post
        fields = "__all__"


class LikeSerializer(serializers.ModelSerializer):

    users = serializers.SlugRelatedField(
        slug_field="username", queryset=get_user_model().objects.all()
    )

    class Meta:
        model = Like
        fields = "__all__"


class DislikeSerializer(serializers.ModelSerializer):

    user = serializers.SlugRelatedField(
        slug_field="username", queryset=get_user_model().objects.all()
    )

    class Meta:
        model = Dislike
        fields = "__all__"
