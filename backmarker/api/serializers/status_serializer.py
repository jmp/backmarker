from rest_framework.serializers import HyperlinkedModelSerializer

from backmarker.models.status import Status


class StatusSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Status
        fields = ["url", "status"]
