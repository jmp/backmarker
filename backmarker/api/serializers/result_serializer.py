from rest_framework.serializers import HyperlinkedModelSerializer

from backmarker.models.result import Result


class ResultSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Result
        fields = [
            "url",
            "race",
            "driver",
            "constructor",
            "number",
            "grid",
            "position",
            "position_text",
            "position_order",
            "points",
            "laps",
            "time",
            "milliseconds",
            "fastest_lap",
            "rank",
            "fastest_lap_time",
            "fastest_lap_speed",
            "status",
        ]
        extra_kwargs = {
            "driver": {"lookup_field": "reference"},
            "constructor": {"lookup_field": "reference"},
        }
