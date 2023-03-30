from rest_framework.routers import DefaultRouter

from .views import UserApiViewSet,UserProfilePhotoApiView

router = DefaultRouter()
router.register(prefix='user',viewset=UserApiViewSet)
router.register(prefix='avatar',viewset=UserProfilePhotoApiView)

urlpatterns = router.urls