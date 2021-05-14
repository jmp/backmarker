from rest_framework.routers import DefaultRouter

from .api.views import StatusViewSet

router = DefaultRouter()
router.register(r"statuses", StatusViewSet)

urlpatterns = router.urls
