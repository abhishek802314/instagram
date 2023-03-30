from rest_framework.routers import DefaultRouter
from django.urls import path

from .views import PostApiViewSet,PostImageApiViewSet,PostLikeApiView,InstagramFeedApiView

router = DefaultRouter()
router.register(prefix='all',viewset=PostApiViewSet)
router.register(prefix='image',viewset=PostImageApiViewSet)
router.register(prefix='like',viewset=PostLikeApiView)

urlpatterns = [
   path('feed/',InstagramFeedApiView.as_view())

]


urlpatterns += router.urls