from rest_framework.routers import DefaultRouter

from .api.views import ConstructorViewSet

router = DefaultRouter()
router.register(r"constructors", ConstructorViewSet)

urlpatterns = router.urls
