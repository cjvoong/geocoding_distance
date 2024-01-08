from geopy.geocoders import Nominatim
from math import radians, sin, cos, sqrt, atan2

def geocode_address(address):
    # Initialize the Nominatim geocoder
    geolocator = Nominatim(user_agent="my_geocoder")

    # Perform geocoding
    location = geolocator.geocode(address)

    if location:
        print(f"Address: {address}")
        print(f"Latitude: {location.latitude}, Longitude: {location.longitude}")
        return location
    else:
        print("Geocoding failed.")
        raise ValueError("Invalid address")

def haversine(location_from, location_to):
    lat1 = location_from.latitude
    lon1 = location_from.longitude
    lat2 = location_to.latitude
    lon2 = location_to.longitude

    # Radius of the Earth in km
    R = 6371.0

    # Convert latitude and longitude from degrees to radians
    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])

    # Calculate the differences in coordinates
    dlat = lat2 - lat1
    dlon = lon2 - lon1

    # Haversine formula
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    # Calculate the distance
    distance = R * c
    return distance

def km_to_miles(kilometers):
    # Conversion factor from kilometers to miles
    conversion_factor = 0.621371

    # Calculate miles
    miles = kilometers * conversion_factor

    return miles

# Example usage
user_address_from = "LS8 1QR"
location_from=geocode_address(user_address_from)

user_address_to = "LS12 3AS"
location_to=geocode_address(user_address_to)

print(f"Distance between {user_address_from} and {user_address_to}: {km_to_miles(haversine(location_from, location_to))} miles")