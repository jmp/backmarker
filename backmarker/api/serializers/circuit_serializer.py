from rest_framework.serializers import HyperlinkedModelSerializer

from backmarker.models.circuit import Circuit


class CircuitSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Circuit
        fields = [
            "url",
            "reference",
            "name",
            "location",
            "country",
            "latitude",
            "longitude",
            "altitude",
            "wiki_url",
        ]
        extra_kwargs = {"url": {"lookup_field": "reference"}}
