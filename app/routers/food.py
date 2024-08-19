from app.services.mobile_food import FoodTrucks, FoodTrucksService
from app.utils.locate_truck import foodInventory
from app.routers.allfoodtruck import limiter
from app.services.auth import AuthService
from app.schemas.fooditems import Menu
from app.routers.api import router
from fastapi import Request

import datetime

@router.post("/foodTrucks/food")
@AuthService
@limiter.limit("60/minute")
@FoodTrucksService
async def foods(request: Request, menu: Menu):
    """
    Endpoint to find food trucks based on a specified food type.
    This asynchronous endpoint receives a menu object containing the food type to search for,
    fetches the list of food trucks from the external service using the `FoodTrucks` function,
    and filters the food trucks based on the specified food type using the `foodInventory` function. 
    It returns a JSON response with the list of food trucks offering the specified food type or 
    a message indicating that no food trucks were found.

    Parameters:
    menu (Menu): A Pydantic model object containing the food type to search for.

    Returns:
    Dict: A dictionary with the status and data, or a message indicating no food trucks were found.
          The response structure varies based on the result:
          - If food trucks are found:
            {
                "status": "success",
                "data": List[Dict],  # List of dictionaries representing food trucks that offer the specified food type
                "timestamp": datetime.datetime  # Current timestamp when the response is generated
            }
          - If no food trucks are found:
            {
                "status": "not_found",
                "message": "No food trucks found for the specified food type",
                "timestamp": datetime.datetime  # Current timestamp when the response is generated
            }

    Raises:
    HTTPException: If the food truck service is unavailable (handled by the `FoodTrucksService` decorator).
    """
    foodtruck_Data = await FoodTrucks()
    user_foodtype = menu.food_type
    
    result = foodInventory(food_trucks=foodtruck_Data,
                           food_type=user_foodtype)
    
    if not result:
        return {
            "status": "not_found",
            "message": "No food trucks found for the specified food type",
            "timestamp": datetime.datetime.now()
        }
    
    return {
        "status": "success",
        "data": result,
        "timestamp": datetime.datetime.now()
    }