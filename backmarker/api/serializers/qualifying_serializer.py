from rest_framework.serializers import HyperlinkedModelSerializer

from backmarker.models.qualifying import Qualifying


class QualifyingSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Qualifying
        fields = [
            "url",
            "race",
            "driver",
            "constructor",
            "number",
            "position",
            "q1",
            "q2",
            "q3",
        ]
        extra_kwargs = {
            "driver": {"lookup_field": "reference"},
            "constructor": {"lookup_field": "reference"},
        }
