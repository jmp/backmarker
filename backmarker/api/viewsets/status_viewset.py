from rest_framework.viewsets import ReadOnlyModelViewSet

from backmarker.models.status import Status
from backmarker.api.serializers.status_serializer import StatusSerializer


class StatusViewSet(ReadOnlyModelViewSet):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
