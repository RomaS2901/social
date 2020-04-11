from django.urls import path, include

from rest_framework.routers import DefaultRouter

from post.views import PostViewSet, LikeViewSet, DislikeViewSet


app_name = "post"

router = DefaultRouter()
router.register("posts", viewset=PostViewSet)
router.register("likes", viewset=LikeViewSet)
router.register("dislikes", viewset=DislikeViewSet)

urlpatterns = [path("", include(router.urls))]
