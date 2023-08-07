from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_create_date():
    data = {"month": 1, "day": 20}
    response = client.post("/dates/", json=data)
    assert response.status_code == 201
    assert "id" in response.json()
    assert response.json()["month"] == "January"
    assert response.json()["day"] == 20
    assert "fact" in response.json()


def test_create_duplicate_date():
    data = {"month": 1, "day": 20}
    response = client.post("/dates/", json=data)
    assert response.status_code == 409


def test_get_dates():
    response = client.get("/dates/")
    assert response.status_code == 200
    assert len(response.json()) > 0


def test_delete_date():
    response = client.delete("/dates/1/", headers={"X-API-KEY": "SECRET_API_KEY"})
    assert response.status_code == 204


def test_delete_nonexistent_date():
    response = client.delete("/dates/999/", headers={"X-API-KEY": "SECRET_API_KEY"})
    assert response.status_code == 404


def test_get_popular():
    response = client.get("/popular/")
    assert response.status_code == 200
    assert len(response.json()) > 0
    assert all(
        "id" in entry and "month" in entry and "days_checked" in entry
        for entry in response.json()
    )
