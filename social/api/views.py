import datetime

from django.shortcuts import render
from django.utils import timezone

from django.db.models.functions import TruncDay
from django.db.models import Count

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from post.models import Like


@api_view(["GET"])
def analytics(request):
    try:
        date_from = datetime.datetime.fromisoformat(request.data["date_from"])
        date_to = datetime.datetime.fromisoformat(request.data["date_to"])
    except KeyError:
        return Response(
            {
                "detail": 'To get like analytics provide "date_from" and "date_to" urlencoded params'
            },
            status=status.HTTP_400_BAD_REQUEST,
        )
    except ValueError:
        return Response(
            {"detail": "Please provide date in ISO format! For e.g YYYY-MM-DD"},
            status=status.HTTP_400_BAD_REQUEST,
        )
    else:
        likes_analytics = (
            Like.objects.filter(created_at__range=[date_from, date_to])
            .values("created_at")
            .annotate(day=TruncDay("created_at"))
            .values("day")
            .annotate(count=Count("day"))
        )
        return Response({"analytics": likes_analytics})
