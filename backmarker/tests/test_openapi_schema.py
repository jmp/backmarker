import pytest
from openapi_tester import SchemaTester

schema_tester = SchemaTester()

ROUTES = [
    "circuits",
    "constructor_results",
    "constructor_standings",
    "constructors",
    "driver_standings",
    "drivers",
    "lap_times",
    "pit_stops",
    "qualifyings",
    "races",
    "results",
]


@pytest.mark.parametrize("route", ROUTES)
@pytest.mark.django_db
def test_circuits_api_validates_against_schema(client, route):
    response = client.get(f"/api/{route}/")
    assert response.status_code == 200
    schema_tester.validate_response(response)


def test_api_schema_is_served(client):
    response = client.get("/api/schema/")
    assert response.status_code == 200


def test_api_docs_are_served(client):
    response = client.get("/api/schema/redoc/")
    assert response.status_code == 200
