from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_date():
    response = client.post("/dates", json={"month": 1, "day": 20})
    assert response.status_code == 201
    assert response.json()["month"] == "January"
    assert response.json()["day"] == 20

def test_get_dates():
    response = client.get("/dates")
    assert response.status_code == 200
    assert len(response.json()) >= 1

def test_delete_date():
    # First, create a date
    create_response = client.post("/dates", json={"month": 2, "day": 15})
    created_id = create_response.json()["id"]

    # Then, delete the created date
    response = client.delete(f"/dates/{created_id}", headers={"X-API-KEY": "SECRET_API_KEY"})
    assert response.status_code == 204

def test_get_popular_months():
    response = client.get("/popular")
    assert response.status_code == 200
    assert len(response.json()) >= 1
