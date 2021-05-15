from rest_framework.serializers import HyperlinkedModelSerializer

from backmarker.models.race import Race


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
        extra_kwargs = {"circuit": {"lookup_field": "reference"}}
