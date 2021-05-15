from rest_framework.serializers import HyperlinkedModelSerializer

from backmarker.models.lap_time import LapTime


class LapTimeSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = LapTime
        fields = [
            "url",
            "race",
            "driver",
            "lap",
            "position",
            "time",
            "milliseconds",
        ]
        extra_kwargs = {"driver": {"lookup_field": "reference"}}
