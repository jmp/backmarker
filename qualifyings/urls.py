from rest_framework.routers import DefaultRouter

from .api.views import QualifyingViewSet

router = DefaultRouter()
router.register(r"qualifyings", QualifyingViewSet)

urlpatterns = router.urls
