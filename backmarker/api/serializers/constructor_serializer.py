from rest_framework.serializers import HyperlinkedModelSerializer

from backmarker.models.constructor import Constructor


class ConstructorSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Constructor
        fields = [
            "url",
            "reference",
            "name",
            "nationality",
            "wiki_url",
        ]
        extra_kwargs = {"url": {"lookup_field": "reference"}}
