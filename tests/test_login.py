import requests as request

def test_login_success():
    payload = {
        'username': 'admin',
        'password': 'admin123'
    }
    response = request.post("http://127.0.0.1:5000/login", data=payload)
    assert response.status_code == 200
    assert "dashboard" in response.text

def test_login_failure():
    payload = {
        'username': 'admin',
        'password': '456'
    }
    response = request.post("http://127.0.0.1:5000/login", data=payload)
    assert response.status_code == 401