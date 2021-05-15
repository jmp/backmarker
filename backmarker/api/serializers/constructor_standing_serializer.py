from rest_framework.serializers import HyperlinkedModelSerializer

from backmarker.models.constructor_standing import ConstructorStanding


class ConstructorStandingSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = ConstructorStanding
        fields = [
            "url",
            "race",
            "constructor",
            "points",
            "position",
            "position_text",
            "wins",
        ]
        extra_kwargs = {"constructor": {"lookup_field": "reference"}}
