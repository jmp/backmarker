from rest_framework.viewsets import ReadOnlyModelViewSet

from backmarker.models.constructor_standing import ConstructorStanding
from backmarker.api.serializers.constructor_standing_serializer import ConstructorStandingSerializer


class ConstructorStandingViewSet(ReadOnlyModelViewSet):
    queryset = ConstructorStanding.objects.all()
    serializer_class = ConstructorStandingSerializer
