from rest_framework.viewsets import ReadOnlyModelViewSet

from ..models import Status
from .serializers import StatusSerializer


class StatusViewSet(ReadOnlyModelViewSet):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
