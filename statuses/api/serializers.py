from rest_framework.serializers import HyperlinkedModelSerializer

from ..models import Status


class StatusSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Status
        fields = ["url", "status"]
