from rest_framework.serializers import HyperlinkedModelSerializer

from backmarker.models.pit_stop import PitStop


class PitStopSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = PitStop
        fields = [
            "url",
            "race",
            "driver",
            "stop",
            "lap",
            "time",
            "duration",
            "milliseconds",
        ]
        extra_kwargs = {"driver": {"lookup_field": "reference"}}
