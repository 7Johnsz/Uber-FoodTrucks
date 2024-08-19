from app.utils.haversine_math import haversine 
from typing import List, Optional, Dict

def nearTruck(food_trucks: List[Dict],
              user_lat: float,
              user_lon: float) -> Optional[Dict]:
    """
    Finds the nearest food truck to the user's location.
    The function scrolls through a list of food trucks and calculates the distance between the user's location and the location of each food truck
    using the Haversine formula. Returns the nearest food truck.

    Parameters:
    food_trucks (List[Dict]): List of dictionaries where each dictionary represents a food truck. Each dictionary must contain the keys
                              'latitude' and 'longitude' keys with numeric values representing the location of the food truck.
    user_lat (float): Latitude of the user's location in degrees.
    user_lon (float): Longitude of the user's location in degrees.

    Returns:
    Optional[Dict]: The nearest food truck to the user's location. If no food truck is found or if the location
                     cannot be processed, returns None.

    Example:
    >>> food_trucks = [
    ...     {'latitude': '52.2296756', 'longitude': '21.0122287', 'name': 'Truck A'},
    ...     {'latitude': '41.8919300', 'longitude': '12.5113300', 'name': 'Truck B'}
    ... ]
    >>> nearTruck(food_trucks, 52.2296756, 21.0122287)
    {'latitude': '52.2296756', 'longitude': '21.0122287', 'name': 'Truck A'}
    """
    
    nearest_truck = None
    min_distance = float('inf')

    for truck in food_trucks:
        try:
            truck_lat = float(truck.get('latitude', 0))
            truck_lon = float(truck.get('longitude', 0))
        except ValueError:
            continue
            
        distance = haversine(user_lat, user_lon, truck_lat, truck_lon)
        if distance < min_distance:
            min_distance = distance
            nearest_truck = truck

    return nearest_truck

def foodInventory(food_trucks: List[Dict], food_type: Optional[str]) -> List[Dict]:
    """
    Filters the list of food trucks to return only those that offer a specific type of food.
    The function checks whether the type of food is present in each food truck's list of food items and returns a list of food trucks
    that offer the specified type of food.

    Parameters:
    food_trucks (List[Dict]): List of dictionaries where each dictionary represents a food truck. Each dictionary must contain the key
                              'fooditems' key with a string of food items offered by the food truck.
    food_type (Optional[str]): Type of food to be filtered. If None, returns all food trucks.

    Returns:
    List[Dict]: List of food trucks offering the specified food type.

    Example:
    >>> food_trucks = [
    ...     {'fooditems': 'Burgers, Fries', 'name': 'Truck A'},
    ...     {'fooditems': 'Pizza, Pasta', 'name': 'Truck B'}
    ... ]
    >>> foodInventory(food_trucks, 'Pizza')
    [{'fooditems': 'Pizza, Pasta', 'name': 'Truck B'}]
    """

    if food_type:
        filtered_trucks = [
            truck for truck in food_trucks
            if food_type.lower() in truck.get('fooditems', '').lower()
        ]
    return filtered_trucks

    