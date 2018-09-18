import pandas as pd
import re
import utils

class NextTrip(object):
    """

    """

    def __init__(self, station, day, time, data):
        """
        """
        self.station = station
        self.day = day
        self.time = time
        self.data = data


    def find_trip(self):
        #search data for station
        self.searched_station = self.data[self.data['stop_name'].str.contains(self.station, flags=re.IGNORECASE, na=False)]
        #search station for which service is running
        self.checked_route = utils.route_check(self.searched_station, self.day, self.time)

        #compare current time with schedule
        next_three = utils.add_sec(self.checked_route)
        next_diff  = utils.add_diff(next_three)
        next_filter = next_diff[next_diff['diff'] > 0]

        #filtered all past trips and keep future trips in sorted dataframe
        final_frame = next_filter.sort_values(by=['diff'])

        #return needed information
        self.next_dep_times = final_frame['departure_time'].head(3).tolist()
        self.next_dep_routes = final_frame['route_id'].head(3).tolist()
        self.headsign = final_frame['trip_headsign'].head(3).tolist()
        self.stop_name = final_frame['stop_name'].head(3).tolist()


        self.stop_id = final_frame['stop_id'].head(3).tolist()


        return (self.next_dep_routes,self.next_dep_times, self.headsign, self.stop_name, self.stop_id)

    def next_departures(self):
        #Print function to show next 3 departures
        self.next_dep_routes, self.next_dep_times, self.headsign, self.stop_name, self.stop_id = self.find_trip()

        print('')
        print("For Station Search: {} on {} at time: {}".format(self.station,self.day, self.time))
        print("Next Departures are at:")
        for i in range(0,len(self.next_dep_routes)):
            print("{}: Route {}: {} at {}, stop id: {}".format(self.next_dep_times[i], self.next_dep_routes[i], self.headsign[i], self.stop_name[i], self.stop_id[i]))

        