from django.contrib.auth import get_user_model

from rest_framework import serializers

from post.models import Post, Like, Dislike
from accounts.serializers import UserSerializer


# class MyStringRelatedField(serializers.StringRelatedField):
#     def to_internal_value(self, data):
#         print(data)
#         return super().to_internal_value(data)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ("username",)


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"


class LikeSerializer(serializers.ModelSerializer):

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
