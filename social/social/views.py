from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


@api_view(["GET"])
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
        }
    )
