from rest_framework.viewsets import ReadOnlyModelViewSet

from backmarker.models.constructor_result import ConstructorResult
from backmarker.api.serializers.constructor_result_serializer import ConstructorResultSerializer


class ConstructorResultViewSet(ReadOnlyModelViewSet):
    queryset = ConstructorResult.objects.all()
    serializer_class = ConstructorResultSerializer
