from rest_framework.routers import DefaultRouter

from .api.views import RaceViewSet

router = DefaultRouter()
router.register(r"races", RaceViewSet)

urlpatterns = router.urls
