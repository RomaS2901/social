from django.contrib.auth import get_user_model

from rest_framework.serializers import ModelSerializer


class UserAPISerializer(ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ("last_login", "date_joined", "username")
