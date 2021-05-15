from rest_framework.viewsets import ReadOnlyModelViewSet

from backmarker.api.serializers.constructor_serializer import ConstructorSerializer
from backmarker.models.constructor import Constructor


class ConstructorViewSet(ReadOnlyModelViewSet):
    queryset = Constructor.objects.all()
    serializer_class = ConstructorSerializer
    lookup_field = "reference"
