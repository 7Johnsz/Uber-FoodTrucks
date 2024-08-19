import math

def haversine(lat1: float,
              lon1: float,
              lat2: float,
              lon2: float) -> float:
    """
    Calculates the distance in kilometers between two points on the Earth's surface using the Haversine formula.
    The Haversine formula is used to calculate the distance between two points on a sphere based on their latitudes and longitudes.

    Parameters:
    lat1 (float): Latitude of the first point in degrees.
    lon1 (float): Longitude of the first point in degrees.
    lat2 (float): Latitude of the second point in degrees.
    lon2 (float): Longitude of the second point in degrees.

    Returns:
    float: The distance between the two points in kilometers.

    Example:
    >>> haversine(52.2296756, 21.0122287, 41.8919300, 12.5113300)
    1317.071
    """
    
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
    c = 2 * math.asin(math.sqrt(a))
    
    r = 6371
    return c * r