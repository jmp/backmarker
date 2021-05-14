from rest_framework.serializers import HyperlinkedModelSerializer

from ..models import Qualifying


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
