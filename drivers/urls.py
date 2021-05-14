from rest_framework.routers import DefaultRouter

from .api.views import DriverViewSet

router = DefaultRouter()
router.register(r"drivers", DriverViewSet)

urlpatterns = router.urls
