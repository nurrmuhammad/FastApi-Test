from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_get_school():
    response = client.get("/api/school")
    assert response.status_code == 200
    assert "data" in response.json()
    assert isinstance(response.json()["data"], list)

def test_get_student():
    response = client.get("/api/student")
    assert response.status_code == 200
    assert "data" in response.json()
    assert isinstance(response.json()["data"], list)

def test_get_school_by_name_found():
    response = client.get("/api/school/PDP School")
    assert response.status_code == 200
    assert "data" in response.json()

def test_get_student_by_name_found():
    response = client.get("/api/student/Nurmuhammad")
    assert response.status_code == 200
    assert "data" in response.json()

def test_get_school_by_name_not_found():
    response = client.get("/api/school/Unknown School")
    assert response.status_code == 200
    assert response.json()["error"] == "School not found"

def test_get_student_by_name_not_found():
    response = client.get("/api/student/Unknown Student")
    assert response.status_code == 200
    assert response.json()["error"] == "Student not found"