from django.urls import include, path
from rest_framework.routers import DefaultRouter

from backmarker.urls import router as backmarker_router

router = DefaultRouter()
router.registry.extend(backmarker_router.registry)

urlpatterns = [
    path("api/", include(router.urls)),
]
