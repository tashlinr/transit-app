## Improved Version of last program.

### Program prints next departures for a given searched station on the NYC-MTA.

#### Updates
Cleaned up code.
Added more user inputs.
Added rudimentary unit testing.


#### User
Change Directory into transit_test_2

Command line:
>>> python main.py [Search Station] [Search Time(optional)] [# of Next Departures(optional)]

ex.
>>> python main.py "Grand Central"
>>> python main.py "Pelham" "2019-11-11 12:10"
>>> python main.py "42 st" "2019-08-08 8:34" "6"


#### Parameters
  Parameters:
  Search Station(str): Station User wants to search departures for.
  Search Time(str): Specific time user wants to search for. 
                    Defaults to current time.
                    Input Format: "%Y-%m-%d %H:%M"  ex. "2018-11-11 12:10"
  # of Next Departures(int): Number of next departures User wants to see.
                   			 Defaults to 3  