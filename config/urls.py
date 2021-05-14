from django.urls import include, path
from rest_framework.routers import DefaultRouter

from circuits.urls import router as circuits_router
from drivers.urls import router as drivers_router
from seasons.urls import router as seasons_router
from statuses.urls import router as statuses_router
from races.urls import router as races_router
from constructors.urls import router as constructors_router
from results.urls import router as results_router

router = DefaultRouter()
router.registry.extend(circuits_router.registry)
router.registry.extend(drivers_router.registry)
router.registry.extend(seasons_router.registry)
router.registry.extend(statuses_router.registry)
router.registry.extend(races_router.registry)
router.registry.extend(constructors_router.registry)
router.registry.extend(results_router.registry)

urlpatterns = [
    path("api/", include(router.urls)),
]
