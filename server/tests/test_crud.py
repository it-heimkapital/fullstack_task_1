import json


def test_department_create(test_app):
    # Test create department
    test_request_payload = {
        "name": "IT"
    }

    response = test_app.post("/api/create_department/", content=json.dumps(test_request_payload),)
    response = response.json()

    assert response["status"] == "success"
    assert response["department"]["name"] == test_request_payload["name"]


def test_employee_create(test_app):
    # Test Employee create here
    response = test_app.post("/api/create_department/", content=json.dumps({"name": "Sales"}),)

    test_request_payload = {
        "first_name": "fast",
        "last_name": "api",
        "department_id": response.json()["department"]["id"]
    }
    response = test_app.post("/api/create_employee/", content=json.dumps(test_request_payload),)

    response = response.json()
    assert response["status"] == "success"
    assert response["employee"]["first_name"] == test_request_payload["first_name"]
    assert response["employee"]["last_name"] == test_request_payload["last_name"]
    assert response["employee"]["department_id"] == test_request_payload["department_id"]


def test_get_employee(test_app):
    # Test get employees
    response = test_app.get("/api/get_employees/")
    response = response.json()

    assert response["status"] == "success"
    assert response["results"] == 1


