def test_hello_world(client):
    response = client.get('/')
    assert response.status_code == 200


def test_hello_name(client):
    response = client.get('/hello/test_user/')
    assert response.status_code == 200
    assert response.json == {"message": f"Hello, test_user!"}
