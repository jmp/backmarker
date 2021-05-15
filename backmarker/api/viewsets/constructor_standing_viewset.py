from rest_framework.viewsets import ReadOnlyModelViewSet

from backmarker.api.serializers.constructor_standing_serializer import (
    ConstructorStandingSerializer,
)
from backmarker.models.constructor_standing import ConstructorStanding


class ConstructorStandingViewSet(ReadOnlyModelViewSet):
    queryset = ConstructorStanding.objects.all()
    serializer_class = ConstructorStandingSerializer
