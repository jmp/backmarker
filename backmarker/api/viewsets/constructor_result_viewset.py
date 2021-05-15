from rest_framework.viewsets import ReadOnlyModelViewSet

from backmarker.api.serializers.constructor_result_serializer import (
    ConstructorResultSerializer,
)
from backmarker.models.constructor_result import ConstructorResult


class ConstructorResultViewSet(ReadOnlyModelViewSet):
    queryset = ConstructorResult.objects.all()
    serializer_class = ConstructorResultSerializer
