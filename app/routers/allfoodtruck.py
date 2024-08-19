from app.services.mobile_food import FoodTrucks, FoodTrucksService
from slowapi.util import get_remote_address
from app.services.auth import AuthService
from app.routers.api import router
from fastapi import Request
from slowapi import Limiter

limiter = Limiter(key_func=get_remote_address)

@router.get("/foodtrucks")
@AuthService
@limiter.limit("60/minute")
@FoodTrucksService
async def trucks(request: Request):
    """
    Endpoint to retrieve the list of food trucks.
    This asynchronous endpoint fetches the current list of food trucks from the external service using
    the `FoodTrucks` function. It returns the food truck data in JSON format, which includes details of
    all available food trucks.

    Returns:
    List[Dict]: A list of dictionaries where each dictionary represents a food truck. The structure of the dictionary includes
                information such as the truck's location, food items offered, and other relevant details.

    Response Structure:
    [
        {
            "applicant": str,        # Name of the food truck applicant
            "address": str,          # Location description of the food truck
            "latitude": str,       # Latitude of the food truck
            "longitude": str,      # Longitude of the food truck
            "fooditems": str         # Food items offered by the food truck
        },
        ...
    ]

    Raises:
    HTTPException: If the food truck service is unavailable (handled by the `FoodTrucksService` decorator).
    """
    return await FoodTrucks()