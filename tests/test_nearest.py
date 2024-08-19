from fastapi.testclient import TestClient
from dotenv import load_dotenv
from app.main import app 
import asyncio
import pytest
import os

load_dotenv()
expected_auth = os.getenv('AUTHORIZATION')

# Set the event loop policy for Windows
asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

@pytest.fixture
def client():
    """
    Fixture to create a test client for the FastAPI application.

    Returns:
        TestClient: An instance of the test client configured with the FastAPI application.
    """
    return TestClient(app)

@pytest.mark.parametrize("payload, expected_status_code", [
    ({"latitude": 37.7749, "longitude": -122.4194}, 200),  # Valid data
    ({"longitude": -122.4194}, 422),  # Missing latitude
    ({"latitude": 37.7749}, 422),  # Missing longitude
    ({"latitude": "invalid", "longitude": -122.4194}, 422),  # Invalid latitude type
    ({"latitude": 37.7749, "longitude": "invalid"}, 422),  # Invalid longitude type
    ({"latitude": 1000, "longitude": -122.4194}, 422),  # Latitude out of range
    ({"latitude": 37.7749, "longitude": 2000}, 422)  # Longitude out of range
])
def test_food_trucks_nearest(client, payload, expected_status_code):
    """
    Test the endpoint for the nearest food truck with various payloads.

    Uses parameterized tests to cover different cases including valid data,
    missing fields, invalid types, and out-of-range values.

    Args:
        client (TestClient): The test client for the FastAPI application.
        payload (dict): The request payload to be sent to the endpoint.
        expected_status_code (int): The expected HTTP status code of the response.
    """
    
    headers = {"Authorization": expected_auth}
    response = client.post("/foodTrucks/nearest", json=payload, headers=headers)
    assert response.status_code == expected_status_code

    if expected_status_code == 200:
        json_response = response.json()
        assert isinstance(json_response, dict), f"Expected dict but got {type(json_response)}"
        assert json_response.get("status") == "success"

        data = json_response.get("data", {})
        assert isinstance(data, dict)
        assert "truck" in data

        truck = data.get("truck")
        assert isinstance(truck, dict)
        assert "applicant" in truck
        assert "address" in truck
        assert "latitude" in truck
        assert "longitude" in truck
        assert "fooditems" in truck
