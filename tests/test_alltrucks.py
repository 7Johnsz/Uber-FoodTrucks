from fastapi.testclient import TestClient
from dotenv import load_dotenv
from app.main import app  
import pytest
import os

load_dotenv()
expected_auth = os.getenv('AUTHORIZATION')

@pytest.fixture
def client():
    """
    Fixture to create a test client for the FastAPI application.

    Returns:
        TestClient: An instance of the test client configured with the FastAPI application.
    """
    return TestClient(app)

def test_food_trucks_endpoint(client):
    """
    Test the /foodtrucks endpoint.

    This test sends a GET request to the /foodtrucks endpoint and verifies that:
    - The response status code is 200.
    - The response is in JSON format.
    - The response contains a list of food trucks, each with the expected fields.

    The test assumes that the endpoint returns a list of dictionaries, each representing a food truck with
    the following fields:
    - "applicant" (str): Name of the food truck applicant.
    - "address" (str): Location description of the food truck.
    - "latitude" (str): Latitude of the food truck.
    - "longitude" (str): Longitude of the food truck.
    - "fooditems" (str): Food items offered by the food truck as a string (optional).

    Args:
        client (TestClient): The test client for the FastAPI application.

    Raises:
        AssertionError: If the response status code is not 200, or the response does not meet the expected format.
    """
    
    headers = {"Authorization": expected_auth}
    response = client.get("/foodtrucks", headers=headers)
    assert response.status_code == 200, f"Expected status code 200 but got {response.status_code}"

    json_response = response.json()
    assert isinstance(json_response, list), f"Expected list but got {type(json_response)}"

    if json_response:
        # Print response for debugging
        print(json_response)

        for i, truck in enumerate(json_response):
            assert isinstance(truck, dict), f"Expected dict but got {type(truck)} in item {i}"
            
            # Check for expected keys
            assert "applicant" in truck, f"Missing 'applicant' field in item {i}"
            assert "address" in truck, f"Missing 'address' field in item {i}"
            assert "latitude" in truck, f"Missing 'latitude' field in item {i}"
            assert "longitude" in truck, f"Missing 'longitude' field in item {i}"
            
            # Check the types of the fields
            assert isinstance(truck["applicant"], str), f"Expected 'applicant' to be str but got {type(truck['applicant'])} in item {i}"
            assert isinstance(truck["address"], str), f"Expected 'address' to be str but got {type(truck['address'])} in item {i}"
            assert isinstance(truck["latitude"], str), f"Expected 'latitude' to be str but got {type(truck['latitude'])} in item {i}"
            assert isinstance(truck["longitude"], str), f"Expected 'longitude' to be str but got {type(truck['longitude'])} in item {i}"
            
            # Skip detailed validation of 'fooditems'
            # Optionally, check if 'fooditems' exists and is a string
            if "fooditems" in truck:
                assert isinstance(truck["fooditems"], str), f"Expected 'fooditems' to be str but got {type(truck['fooditems'])} in item {i}"
