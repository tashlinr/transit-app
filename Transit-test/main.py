from nextTrip import NextTrip
from merger import merge_data
import sys     
import utils

def main():


    data = merge_data()


    station_input = str(sys.argv[1])
    day, now = utils.date_time_info()


    f1 = NextTrip(station_input,day, now,data)

    

    return f1.next_departures()






























if __name__ == '__main__':
    main()