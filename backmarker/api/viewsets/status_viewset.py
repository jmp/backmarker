from rest_framework.viewsets import ReadOnlyModelViewSet

from backmarker.api.serializers.status_serializer import StatusSerializer
from backmarker.models.status import Status


class StatusViewSet(ReadOnlyModelViewSet):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
