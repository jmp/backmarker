from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView
from rest_framework.routers import DefaultRouter

from backmarker.urls import router as backmarker_router

router = DefaultRouter()
router.registry.extend(backmarker_router.registry)

urlpatterns = [
    path("api/", include(router.urls)),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "api/schema/redoc/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),
]
