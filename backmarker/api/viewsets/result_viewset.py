from rest_framework.viewsets import ReadOnlyModelViewSet

from backmarker.models.result import Result
from backmarker.api.serializers.result_serializer import ResultSerializer


class ResultViewSet(ReadOnlyModelViewSet):
    queryset = Result.objects.all()
    serializer_class = ResultSerializer
