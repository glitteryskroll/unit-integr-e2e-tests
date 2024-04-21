import requests
from ..server.url_adress import url

def test_get_index_route():
    response = requests.get(url)
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, World!"}

def test_creating_item_object():
    response = requests.get(url + "items/456?q=test")
    assert response.status_code == 200
    assert response.json() == {"item_id": 456, "q": "test"}

def test_calucalting_cube():
    response = requests.get(url + "cube/2")
    assert response.status_code == 200
    assert response.json()['result'] == 8