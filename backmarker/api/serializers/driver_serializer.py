from rest_framework.serializers import HyperlinkedModelSerializer

from backmarker.models.driver import Driver


class DriverSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Driver
        fields = [
            "url",
            "reference",
            "number",
            "code",
            "first_name",
            "last_name",
            "date_of_birth",
            "nationality",
            "wiki_url",
        ]
        extra_kwargs = {"url": {"lookup_field": "reference"}}
