from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.reverse import reverse


@api_view(["GET"])
@permission_classes([AllowAny])
def root_api_view(request, format=None):
    return Response(
        {
            "token-obtain-pair": reverse(
                "accounts:token-obtain-pair", request=request, format=format
            ),
            "token-refresh": reverse(
                "accounts:token-refresh", request=request, format=format
            ),
            "token-verify": reverse(
                "accounts:token-verify", request=request, format=format
            ),
            "signup": reverse("accounts:signup", request=request, format=format),
            "posts": reverse("post:post-list", request=request, format=format),
            "likes": reverse("post:like-list", request=request, format=format),
            "dislikes": reverse("post:dislike-list", request=request, format=format),
        }
    )
