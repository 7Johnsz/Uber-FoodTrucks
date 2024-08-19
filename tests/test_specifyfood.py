from fastapi.testclient import TestClient
from app.schemas.fooditems import Menu
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

def test_foods_endpoint(client):
    """
    Test the /foodTrucks/food endpoint.

    This test sends a POST request to the /foodTrucks/food endpoint with a specified food type,
    and verifies that:
    - The response status code is 200.
    - The response is in JSON format.
    - The response contains a status and timestamp fields.
    - If the food type is found, the response contains a list of food trucks in the data field.
    - If the food type is not found, the response contains a message indicating no food trucks were found.

    The test assumes that the endpoint expects a JSON payload with the following structure:
    {
        "food_type": "string"
    }

    Args:
        client (TestClient): The test client for the FastAPI application.

    Raises:
        AssertionError: If the response status code is not 200, or the response does not meet the expected format.
    """
    # Define the payload for the test
    payload = {"food_type": "Tacos"}
    
    # Send the POST request
    headers = {"Authorization": expected_auth}
    response = client.post("/foodTrucks/food", json=payload, headers=headers)
    
    # Check that the response status code is 200
    assert response.status_code == 200

    # Parse the JSON response
    json_response = response.json()

    # Check that the response is in JSON format
    assert isinstance(json_response, dict), f"Expected dict but got {type(json_response)}"

    # Check for the presence of the status and timestamp fields
    assert "status" in json_response, "Missing 'status' field"
    assert "timestamp" in json_response, "Missing 'timestamp' field"

    # Depending on whether food trucks are found or not, validate the response structure
    if json_response["status"] == "success":
        assert "data" in json_response, "Missing 'data' field when status is 'success'"
        assert isinstance(json_response["data"], list), f"Expected list but got {type(json_response['data'])}"
        # Additional checks can be added here to validate the contents of the 'data' list
    elif json_response["status"] == "not_found":
        assert "message" in json_response, "Missing 'message' field when status is 'not_found'"
        assert json_response["message"] == "No food trucks found for the specified food type", "Incorrect 'message' content"
    else:
        raise AssertionError("Unexpected 'status' value")

