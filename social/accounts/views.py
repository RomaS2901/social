from django.contrib.auth import get_user_model, authenticate

from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.decorators import api_view
from rest_framework.permissions import AllowAny

from accounts.serializers import UserSerializer


class SignUp(CreateAPIView):

    model = get_user_model()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]
