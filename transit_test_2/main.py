from findroute import FindRoute
import sys

def main():


  if len(sys.argv) == 2:
    station_input = str(sys.argv[1])
    next_departures = FindRoute(station_input)
  elif len(sys.argv) == 3:
    station_input, time_input = str(sys.argv[1]), str(sys.argv[2])
    next_departures = FindRoute(station_input, time_input)
  elif len(sys.argv) == 4:
    station_input, time_input, num_station_input = str(sys.argv[1]), str(sys.argv[2]), int(sys.argv[3])
    next_departures = FindRoute(station_input, time_input, num_station_input)
  else:
      print("Input Error")
      return 
  print(next_departures.print_next_departures())




if __name__ == '__main__':
  main()