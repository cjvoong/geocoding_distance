import unittest
from unittest.mock import patch
from unittest.mock import Mock
from distance_calculator import DistanceCalculator

class TestDistanceCalculator(unittest.TestCase):

    def setUp(self):
        self.distance_calculator = DistanceCalculator()

    @patch('geopy.geocoders.Nominatim.geocode')
    def test_geocode_address_success(self, mock_geocode):
        mock_location = mock_geocode.return_value
        mock_location.latitude = 40.7128
        mock_location.longitude = -74.0060

        address = "New York, NY"
        result = self.distance_calculator.geocode_address(address)

        self.assertEqual(result.latitude, 40.7128)
        self.assertEqual(result.longitude, -74.0060)

    @patch('geopy.geocoders.Nominatim.geocode')
    def test_geocode_address_failure(self, mock_geocode):
        mock_geocode.return_value = None

        address = "Invalid Address"
        with self.assertRaises(ValueError):
            self.distance_calculator.geocode_address(address)

    def test_haversine(self):
        # You can add more test cases for this method
        lon1 = -74.0060
        lat1 = 40.7128
        lon2 = -73.9667
        lat2 = 40.78

        result = self.distance_calculator.haversine(lat1,lon1, lat2,lon2)
        self.assertAlmostEqual(result, 5.08, places=2)

    def test_find_nearest_locations(self):
        # Mock the geocode_address and haversine methods if needed
        # postcodes = ["LS12 3AS","LS1 4HR","LS1 2TW","LS11 8LU","YO1 0SB"]
        # locations = list(map(lambda x: self.distance_calculator.geocode_address(x), postcodes))

        locations = [
            {
                "id": 1,
                "latitude": 53.7982382,
                "longitude": -1.587798
            },
            {
                "id": 2,
                "latitude": 53.795208425,
                "longitude": -1.551847875
            },
            {
                "id": 3,
                "latitude": 53.79716893333334,
                "longitude": -1.55455285
            },
            {
                "id": 4,
                "latitude": 53.75815165499999,
                "longitude": -1.5746591650000001
            },
            {
                "id": 5,
                "latitude": 53.95963,
                "longitude": -1.08563
            }
        ]
        print(locations)
        user_address_from = "LS8 1QR"
        max_distance = 5

        result = self.distance_calculator.find_nearest_locations_postcode(user_address_from, locations, max_distance)
        # Add your assertions based on the expected output
        expected_result=[{'id': 1, 'latitude': 53.7982382, 'longitude': -1.587798, 'distance': 3.7247795687565812}, {'id': 2, 'latitude': 53.795208425, 'longitude': -1.551847875, 'distance': 3.0142142616151673}, {'id': 3, 'latitude': 53.79716893333334, 'longitude': -1.55455285, 'distance': 2.9423108004072263}]
        self.assertEqual(len(result), 3)

if __name__ == '__main__':
    unittest.main()
