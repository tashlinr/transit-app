import sys
import re
import pandas as pd
import datetime, time




def read_data():
    #read in txt files needed from GTFS
    routes  = pd.read_csv("routes.txt",delimiter=",")
    trips = pd.read_csv("trips.txt",delimiter=",")
    stop_times = pd.read_csv("stop_times.txt",delimiter=",")
    stops = pd.read_csv("stops.txt",delimiter=",")
    calendar = pd.read_csv("calendar.txt", delimiter = ",")
    return(routes, trips, stop_times, stops, calendar)


def merge_data():
    #merge the data for usage
    routes, trips, stop_times, stops, calendar = read_data()
    #first merge routes and trip ON route_id
    mer = pd.merge(routes, trips, how='inner', on='route_id', left_on=None, right_on=None,
    left_index=False, right_index=False, sort=True)

    #Second merge new table with stop_times ON trip_id from the trip table
    mer2 = pd.merge(mer,stop_times , how='inner', on='trip_id', left_on=None, right_on=None,
    left_index=False, right_index=False, sort=True)

    # Third merge new table with stops ON stop_id from stop_times table
    mer3 = pd.merge(mer2,stops , how='inner', on='stop_id', left_on=None, right_on=None,
    left_index=False, right_index=False, sort=True)
    mer4 = pd.merge(mer3,calendar , how='inner', on='service_id', left_on=None, right_on=None,
    left_index=False, right_index=False, sort=True)
    return (mer4, calendar)




def add_sec(checked_route):
    #add seconds column to data for easy comparison to Now time.
    temp_seconds = pd.DataFrame() 
    temp_seconds['seconds'] = checked_route['departure_time'].apply(get_sec) 
    result = pd.concat([checked_route, temp_seconds], axis=1)
    return(result)


def add_diff(next_three):
    #Compare time Now to Schedule
    temp_diff = pd.DataFrame()
    temp_diff['diff'] = next_three['seconds'].apply(get_diff)
    result = pd.concat([next_three, temp_diff], axis=1)
    return(result)


def get_sec(time_str):
    #convert current time string to seconds
    h, m, s = time_str.split(':')
    return (int(h) * 3600 + int(m) * 60 + int(s))


def get_diff(time_seconds):
    # find difference of current time to scheduled times 
    now = datetime.datetime.now()
    midnight = now.replace(hour=0, minute=0, second=0, microsecond=0)
    seconds = (now - midnight).seconds
    return (time_seconds - seconds)


def date_time_info():    
    weekday_list = ['monday','tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    day_str  = weekday_list[datetime.date.today().weekday()]
    time_now = datetime.datetime.fromtimestamp(time.time()).strftime('%H:%M:%S')
    return (day_str, time_now)


def route_check(searched_station, day_str, time_now):
    return (searched_station[searched_station[day_str]==True])
