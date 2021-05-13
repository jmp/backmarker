from rest_framework.routers import DefaultRouter

from .api.views import CircuitViewSet

router = DefaultRouter()
router.register(r"circuits", CircuitViewSet)

urlpatterns = router.urls
