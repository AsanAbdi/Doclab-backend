from rest_framework import routers

from apps.posts.views import PostAPIView

router = routers.DefaultRouter()
router.register('posts', PostAPIView)

urlpatterns = router.urls