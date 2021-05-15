from rest_framework.viewsets import ReadOnlyModelViewSet

from backmarker.models.constructor import Constructor
from backmarker.api.serializers.constructor_serializer import ConstructorSerializer


class ConstructorViewSet(ReadOnlyModelViewSet):
    queryset = Constructor.objects.all()
    serializer_class = ConstructorSerializer
    lookup_field = "reference"
