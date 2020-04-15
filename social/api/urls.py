from django.urls import path
from api import views


app_name = "api"

urlpatterns = [
    path("analytics/", views.analytics, name="analytics"),
    path("user_activity/", views.user_activity, name="user-activity"),
]
