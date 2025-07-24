import requests as request

def test_api_status():
    response = request.get("http://127.0.0.1:5000/api/status")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "ok"
    assert data["projecting"] is True
    assert data["connected"] is True