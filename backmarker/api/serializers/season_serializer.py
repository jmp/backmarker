from rest_framework.serializers import HyperlinkedModelSerializer

from backmarker.models.season import Season


class SeasonSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Season
        fields = [
            "url",
            "year",
            "wiki_url",
        ]
