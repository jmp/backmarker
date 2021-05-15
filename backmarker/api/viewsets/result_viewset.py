from rest_framework.viewsets import ReadOnlyModelViewSet

from backmarker.api.serializers.result_serializer import ResultSerializer
from backmarker.models.result import Result


class ResultViewSet(ReadOnlyModelViewSet):
    queryset = Result.objects.all()
    serializer_class = ResultSerializer
