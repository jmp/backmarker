from rest_framework.serializers import HyperlinkedModelSerializer

from ..models import Race


class RaceSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Race
        fields = [
            "url",
            "year",
            "round",
            "circuit",
            "name",
            "date",
            "time",
            "wiki_url",
        ]
