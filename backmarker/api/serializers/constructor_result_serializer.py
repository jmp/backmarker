from rest_framework.serializers import HyperlinkedModelSerializer

from backmarker.models.constructor_result import ConstructorResult


class ConstructorResultSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = ConstructorResult
        fields = [
            "url",
            "race",
            "constructor",
            "points",
            "status",
        ]
        extra_kwargs = {"constructor": {"lookup_field": "reference"}}
