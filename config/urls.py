from django.urls import include, path
from rest_framework.routers import DefaultRouter

from circuits.urls import router as circuits_router
from drivers.urls import router as drivers_router

router = DefaultRouter()
router.registry.extend(circuits_router.registry)
router.registry.extend(drivers_router.registry)

urlpatterns = [
    path("api/", include(router.urls)),
]
