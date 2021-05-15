from rest_framework.serializers import HyperlinkedModelSerializer

from backmarker.models.driver_standing import DriverStanding


class DriverStandingSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = DriverStanding
        fields = [
            "url",
            "race",
            "driver",
            "points",
            "position",
            "position_text",
            "wins",
        ]
        extra_kwargs = {"driver": {"lookup_field": "reference"}}
