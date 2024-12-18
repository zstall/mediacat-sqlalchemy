import pytest
import sys
import os
from main import app

@pytest.fixture
def client():
    """A test client for the app."""
    with app.test_client() as client:
        yield client

def test_home(client):
    """Test the home route."""
    response = client.get('/')
    assert response.status_code == 200
    

# def test_about(client):
#     """Test the about route."""
#     response = client.get('/login')
#     assert response.status_code == 200

# def test_multiply(client):
#     """Test the multiply route with valid input."""
#     response = client.get('/wlak_dir')
#     assert response.status_code == 200

# def test_non_existent_route(client):
#     """Test for a non-existent route."""
#     response = client.get('/non-existent')
#     assert response.status_code == 404