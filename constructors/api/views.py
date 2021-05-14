from rest_framework.viewsets import ReadOnlyModelViewSet

from ..models import Constructor
from .serializers import ConstructorSerializer


class ConstructorViewSet(ReadOnlyModelViewSet):
    queryset = Constructor.objects.all()
    serializer_class = ConstructorSerializer
    lookup_field = "reference"
