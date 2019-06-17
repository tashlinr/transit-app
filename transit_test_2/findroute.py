from datetime import datetime
import pandas as pd
import re


class FindRoute:
  """
  A class to find the next departures of a searched station in NYC.


  Parameters:
  argument1 (str): Station User wants to search departures for.
  argument2 (str): Specific time user wants to search for. 
                   Defaults to current time.
                   Input Format: "%Y-%m-%d %H:%M"  ex. "2018-11-11 12:10"
  argument3 (int): Number of next departures User wants to see.
                   Defaults to 3 

  Returns: 
  Pandas Dataframe of next searched departures and the routes.

  """
  def __init__(self, station, search_time = datetime.now(), num_next_departures = 3):
    self.station = station
    self.search_time = search_time
    self.num_next_departures = num_next_departures


  def __repr__(self):
    return f'FindRoute("{self.station}", datetime({self.search_time:%-Y, %-m, %-d, %-H, %-M, %-S, %f}))'
    

  def __str__(self):
    return f'Find Next Routes at {self.search_time:%H:%M:%S} on {self.search_time:%b/%d/%y} for {self.station}'


  def get_merged_gtfs(self):
    """Create one Dataframe from merging GTFS data."""
    filepath_gtfs = "GTFS/"
    try:
      routes  = pd.read_csv(filepath_gtfs + "routes.txt")
      trips = pd.read_csv(filepath_gtfs + "trips.txt")
      stop_times = pd.read_csv(filepath_gtfs + "stop_times.txt")
      stops = pd.read_csv(filepath_gtfs + "stops.txt")
      calendar = pd.read_csv(filepath_gtfs + "calendar.txt")
      return routes.merge(trips, on='route_id').merge(stop_times, on='trip_id')\
                   .merge(stops, on='stop_id').merge(calendar, on='service_id')

    except FileNotFoundError:
      raise FileNotFoundError("Incorrect GTFS filepath or format")


  def get_station_data(self):
    """Filter Dataframe for Station."""
    if len(self.station) <= 2:
      raise ValueError("Please input a more descript search station (greater than 3 digits)") 
    all_route_data = self.get_merged_gtfs()      
    return all_route_data[all_route_data['stop_name'].str.contains(self.station, flags=re.IGNORECASE, na=False)]


  def get_same_day_routes(self):
    """Filter Dataframe for weekday that routes run."""
    station_route_data = self.get_station_data()
    if station_route_data.empty:
      raise ValueError("Searched station not found, please try another")

    if type(self.search_time) != type(datetime.now()):
      self.convert_search_time()
    print(f'Searching {self.num_next_departures} next departures for Station: {self.station} at {self.search_time:%H:%M:%S} ')
    return station_route_data[station_route_data[self.search_time.strftime("%A").lower()]==1]
    

  def get_next_departures(self):
    """Filter Dataframe for next times according to searched time.""" 
    day_route_data = self.get_same_day_routes()
    if not day_route_data.empty:
      return day_route_data[day_route_data["departure_time"]>=self.search_time.strftime("%H:%M:%S")].sort_values(by='departure_time')
    else:
      raise ValueError("No Departures on search day, please try another")
      

  def print_next_departures(self):
    """Print number of next departures according to number input."""
    if self.num_next_departures >= 1 and self.num_next_departures <=10:
      next_departures = self.get_next_departures()
      if not next_departures.empty:
        return f'{next_departures.head(self.num_next_departures)[["departure_time", "route_id", "route_long_name", "stop_name", "trip_headsign"]].reset_index(drop=True)}'
      else:
        raise ValueError("No Departures for search time on specific date, please try another")
    else: 
      raise IndexError("Next departures limited to between 1 and 10")


  def convert_search_time(self):
    """Convert input search time to datetime object."""
    try:
        self.search_time = datetime.strptime(self.search_time, "%Y-%m-%d %H:%M")
        return self.search_time
    except ValueError:
        raise ValueError("Incorrect data format, should be YYYY-MM-DD HH:mm")
    
    
