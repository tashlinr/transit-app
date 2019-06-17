import unittest
from findroute import FindRoute
from datetime import datetime

class testFindRoute(unittest.TestCase):

  @classmethod
  def setUpClass(cls):
      print('setupClass')

  @classmethod
  def tearDownClass(cls):
      print('teardownClass')

  def setUp(self):
      print('setUp')
      self.trip_1 = FindRoute("Grand Central", "2019-06-03 22:10")
      self.trip_2 = FindRoute("Grand Central", "2019-06-03 22:10:4")
      self.trip_3 = FindRoute("Improbable station")
      self.trip_4 = FindRoute(" ")
      self.trip_5 = FindRoute("-5")
      self.trip_6 = FindRoute("Pelham", "2019-06-03 26:10")
      self.trip_7 = FindRoute("Pelham", "2019-06-03 26:10", 15)


  def tearDown(self):
      print('tearDown\n')

  def test_get_merged_gtfs(self):
    print("test_get_merged_gtfs")
    column_names = ['route_id', 'agency_id', 'route_short_name', 
                    'route_long_name', 'route_desc', 'route_type', 
                    'route_url', 'route_color', 'route_text_color', 
                    'service_id', 'trip_id', 'trip_headsign', 'direction_id', 
                    'block_id', 'shape_id', 'arrival_time', 'departure_time', 
                    'stop_id', 'stop_sequence', 'stop_headsign', 'pickup_type', 
                    'drop_off_type', 'shape_dist_traveled', 'stop_code', 'stop_name', 
                    'stop_desc', 'stop_lat', 'stop_lon', 'zone_id', 'stop_url', 
                    'location_type', 'parent_station', 'monday', 'tuesday', 
                    'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 
                    'start_date', 'end_date']

    self.assertCountEqual(self.trip_1.get_merged_gtfs().columns.to_list(), column_names)

  def test_get_station_data(self):
    print("test_get_station_data")
    with self.assertRaises(ValueError):
      self.trip_4.get_station_data()
    with self.assertRaises(ValueError):
      self.trip_5.get_same_day_routes()

  def test_get_same_day_routes(self):
    print("test_get_same_day_routes")

    with self.assertRaises(ValueError):
      self.trip_3.get_same_day_routes()


  def test_print_next_departures(self):
    print("test_print_next_departures")
    with self.assertRaises(IndexError):
      self.trip_7.print_next_departures()


  def test_convert_search_time(self):
    print("test_convert_search_time")
    self.assertEqual(self.trip_1.convert_search_time(), datetime(2019, 6, 3, 22, 10))

    with self.assertRaises(ValueError):
      self.trip_2.convert_search_time()
    with self.assertRaises(ValueError):
      self.trip_6.convert_search_time()



if __name__ == '__main__':
  unittest.main()