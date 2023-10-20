"""
Daniel Gregorio
Riot Games Leaderboard app
"""
import os

import pytest

import app


# Create a fixture called "client" to set up the Flask app for testing
@pytest.fixture
def client():
    # Set the Flask app's configuration to testing mode
    app.app.config['TESTING'] = True
    # Create a test client to interact with the app
    with app.app.test_client() as client:
        # Yield the client object to the test functions
        yield client

# Test for the home page route ('/')
def test_index_route(client):
    # Send a GET request to the home page route
    response = client.get('/')
    # Check if the response status code is 200 (OK)
    assert response.status_code == 200
    # Check if the response data contains the name "Daniel Gregorio"

# Test for the 'valLeaders' route ('/valLeaders')
def test_valLeaders_route(client):
    # Send a GET request to the 'valLeaders' route
    response = client.get('/valLeaders')
    # Check if the response status code is 200 (OK)
    assert response.status_code == 200
    # Additional specific assertions can be added here to validate the API response

# Test for the 'lolLeaders' route ('/lolLeaders')
def test_lolLeaders_route(client):
    # Send a GET request to the 'lolLeaders' route
    response = client.get('/lolLeaders')
    # Check if the response status code is 200 (OK)
    assert response.status_code == 200
    # Additional specific assertions can be added here to validate the API response
