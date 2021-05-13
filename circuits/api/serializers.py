from rest_framework.relations import HyperlinkedIdentityField
from rest_framework.serializers import HyperlinkedModelSerializer

from ..models import Circuit


class CircuitSerializer(HyperlinkedModelSerializer):
    url = HyperlinkedIdentityField(
        view_name="circuits:circuit-detail",
        lookup_field="reference",
    )

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
