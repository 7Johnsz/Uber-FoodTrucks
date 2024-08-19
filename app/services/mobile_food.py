from fastapi import HTTPException
import aiohttp
from aiohttp.client_exceptions import ClientResponseError
from functools import wraps

async def FoodTrucks():
    """
    Fetches the list of food trucks from the San Francisco Open Data API.
    This function makes an asynchronous HTTP GET request to the San Francisco Open Data API to retrieve the current list of food trucks.
    If the request is successful, it returns the food truck data in JSON format. If there is an issue with the request, it raises
    an HTTPException with a status code of 503.

    Returns:
    List[Dict]: A list of dictionaries where each dictionary represents a food truck.

    Raises:
    HTTPException: If the service is unavailable or an unexpected error occurs.
    """
    async with aiohttp.ClientSession() as session:
        try:
            async with session.get("https://data.sfgov.org/resource/rqzj-sfat.json") as response:
                response.raise_for_status()
                food_data = await response.json()
                return food_data  
        except ClientResponseError:
            raise HTTPException(status_code=503, detail="Food truck service is currently unavailable")
        except Exception as e:
            raise HTTPException(status_code=503, detail="An unexpected error occurred")

def FoodTrucksService(func):
    """
    A decorator to ensure that the food truck service is available before executing the wrapped function.
    This decorator first checks if the food truck service is available by calling the `FoodTrucks` function. If the service is
    available, it proceeds to execute the wrapped function. Otherwise, it raises an HTTPException with a status code of 503.

    Parameters:
    func (Callable): The function to be wrapped and checked for service availability.

    Returns:
    Callable: The wrapped function with service availability check.

    Raises:
    HTTPException: If the service is unavailable.
    """
    @wraps(func)
    async def wrapper(*args, **kwargs):
        if await FoodTrucks(): 
            return await func(*args, **kwargs)
        else:
            raise HTTPException(status_code=503, detail="Service unavailable")
    return wrapper