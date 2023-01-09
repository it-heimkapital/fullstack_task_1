import json


def test_create_user(client):
    data = {"first_name": "testuser", "last_name": "lastname", "department_id": 3}
    response = client.post("/employee/create/", json=data)
    assert response.status_code == 200
    assert response.json()["first_name"] == "testuser"
    assert response.json()["department_id"] == 3


def test_read_employee(client):
    data = {
        "first_name": "John",
        "last_name": "Wick",
        "department_id": 2,
        }
    response = client.post("/employee/create/", json=data)
    response = client.get("/employee/get/1/")
    assert response.status_code == 200
    assert response.json()['first_name'] == "John"


def test_read_all_employees(client):
    data = {
        "first_name": "John",
        "last_name": "Wick",
        "department_id": 2,
    }
    client.post("/employee/create/", json=data)
    client.post("/employee/create/", json=data)
    response = client.get("/employee/all")

    assert response.status_code == 200
    assert response.json()[0]
    assert response.json()[1]
