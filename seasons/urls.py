from rest_framework.routers import DefaultRouter

from .api.views import SeasonViewSet

router = DefaultRouter()
router.register(r"seasons", SeasonViewSet)

urlpatterns = router.urls
