def test_api_schema_is_served(client):
    response = client.get("/api/schema/")
    assert response.status_code == 200


def test_api_docs_are_served(client):
    response = client.get("/api/schema/redoc/")
    assert response.status_code == 200
