from geopy.geocoders import Nominatim
from math import radians, sin, cos, sqrt, atan2


class DistanceCalculator: 

    # This is the only method subject to fair use policy, to be called on every new customer registration
    def geocode_address(self,address):
        # Initialize the Nominatim geocoder
        geolocator = Nominatim(user_agent="my_geocoder")

        print(f"Attempting to geocode address: {address}")
        # Perform geocoding
        location = geolocator.geocode(address)

        if location:
            print(f"Address: {address}")
            print(f"Latitude: {location.latitude}, Longitude: {location.longitude}")
            return location
        else:
            print(f"Geocoding failed for address: {address}")
            raise ValueError(f"Invalid address {address}")

    # Go to town on calls to this one
    def haversine(self,lat1,lon1, lat2,lon2):
        # Radius of the Earth in km
        R = 3959 # radius of Earth in miles

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
    
    # returns a dict object containing all the locations where they are within the distance and the distance away
    def find_nearest_locations(self,user_address_from_lat,user_address_from_long, locations, max_distance):        
        # Filter locations within the specified distance
        filtered_locations = []
        
        for location in locations:
            distance = self.haversine(user_address_from_lat,user_address_from_long,location['latitude'],location['longitude'])
            if distance <= max_distance:
                filtered_locations.append({
                    'id': location['id'],
                    'latitude': location['latitude'],
                    'longitude': location['longitude'],
                    'distance': distance
                })

        return filtered_locations

    def find_nearest_locations_postcode(self,user_address_from, locations, max_distance):
        location_from = self.geocode_address(user_address_from)
        return self.find_nearest_locations(location_from.latitude,location_from.longitude, locations, max_distance)
