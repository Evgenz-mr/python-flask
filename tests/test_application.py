from application import app


def test_health():
    client = app.test_client()
    response = client.get('/health')
    assert response.status_code == 200
    assert response.get_json()['status'] == 'ok'


def test_metrics():
    client = app.test_client()
    response = client.get('/metrics')
    assert response.status_code == 200
    assert b'flask_http_requests_total' in response.data
