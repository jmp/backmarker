from rest_framework.viewsets import ReadOnlyModelViewSet

from ..models import Result
from .serializers import ResultSerializer


class ResultViewSet(ReadOnlyModelViewSet):
    queryset = Result.objects.all()
    serializer_class = ResultSerializer
