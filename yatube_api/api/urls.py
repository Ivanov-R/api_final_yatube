from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet

router = DefaultRouter()
router.register("posts", PostViewSet)
router.register("groups", GroupViewSet)
router.register(
    "follow",
    FollowViewSet,
    basename="follows",
)
router.register(
    r"posts/(?P<post_id>[^/.]+)/comments",
    CommentViewSet,
    basename="comments",
)

urlpatterns = [
    path("v1/", include(router.urls)),
    path("v1/", include("djoser.urls")),
    path("v1/", include("djoser.urls.jwt")),
]
