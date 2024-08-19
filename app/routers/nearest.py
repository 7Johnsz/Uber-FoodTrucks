from app.services.mobile_food import FoodTrucks, FoodTrucksService
from app.routers.allfoodtruck import limiter
from app.utils.locate_truck import nearTruck
from app.services.auth import AuthService
from app.schemas.locate import Location
from app.routers.api import router
from fastapi import Request

import datetime

@router.post("/foodTrucks/nearest")
@AuthService
@limiter.limit("60/minute")
@FoodTrucksService
async def nearest_truck(request: Request, location: Location):
    """
    Endpoint to find the nearest food truck based on the user's location.
    This asynchronous endpoint receives a location object containing latitude and longitude,
    fetches the list of food trucks from the external service using the `FoodTrucks` function,
    and determines the nearest food truck using the `nearTruck` function. It returns a JSON response
    with the details of the nearest food truck along with the current timestamp.

    Parameters:
    location (Location): A Pydantic model object containing the latitude and longitude of the user's location.

    Returns:
    Dict: A dictionary containing the status, data, and timestamp. The data includes details of
          the nearest food truck.

    Response Structure:
    {
        "status": "success",
        "data": {
            "truck": {
                "applicant": str,        # Name of the food truck applicant
                "address": str,          # Location description of the food truck
                "latitude": float,       # Latitude of the food truck
                "longitude": float,      # Longitude of the food truck
                "fooditems": str         # Food items offered by the food truck
            }
        },
        "timestamp": str             # Current timestamp when the response is generated
    }

    Raises:
    HTTPException: If the food truck service is unavailable (handled by the `FoodTrucksService` decorator).
    """
    latitude = location.latitude
    longitude = location.longitude

    foodtruck_Data = await FoodTrucks()
    
    result = nearTruck(food_trucks=foodtruck_Data,
                       user_lat=latitude,
                       user_lon=longitude)

    if result:
        response = {
            "status": "success",
            "data": {
                "truck": {
                    "applicant": result.get('applicant'),
                    "address": result.get('locationdescription'),
                    "latitude": float(result.get('latitude', 0)),  
                    "longitude": float(result.get('longitude', 0)), 
                    "fooditems": result.get('fooditems')
                }
            },
            "timestamp": datetime.datetime.now().isoformat(),  # Convertendo para string ISO format
        }
    else:
        response = {
            "status": "not_found",
            "message": "No nearest truck found."
        }

    return response
