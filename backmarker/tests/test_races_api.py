import pytest
from openapi_tester import SchemaTester

schema_tester = SchemaTester()


@pytest.mark.django_db
def test_races_api_validates_against_schema(client):
    response = client.get("/api/races/")
    assert response.status_code == 200
    schema_tester.validate_response(response)
