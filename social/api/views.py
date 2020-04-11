import datetime

from django.shortcuts import render
from django.utils import timezone

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from post.models import Like


@api_view(["GET"])
def analytics(request):
    try:
        # as from client we get only naive date in ISO format...
        # And date will be YYYY-MM-DD 00:00:00,
        # so if Like was created today it won't be included to the analytics for that day because of the time...
        # as it starts to count from beginning of "date_to"... And need to extend "date_to"
        # to max 23:59:59 time to get Likes for a full date as requested.
        date_from = datetime.datetime.combine(
            datetime.datetime.fromisoformat(request.data["date_from"]),
            datetime.time.min,
            tzinfo=timezone.get_current_timezone(),
        )
        date_to = datetime.datetime.combine(
            datetime.datetime.fromisoformat(request.data["date_to"]),
            datetime.time.max,
            tzinfo=timezone.get_current_timezone(),
        )
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
        likes_analytics = Like.objects.filter(created_at__range=[date_from, date_to])
        return Response(likes_analytics.count())
