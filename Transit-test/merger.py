import sys
import re
import pandas as pd
import datetime, time



def merge_data():
    routes, trips, stop_times, stops, calendar = read_data()
    mer = pd.merge(routes, trips, how='inner', on='route_id', left_on=None, right_on=None,
        left_index=False, right_index=False, sort=True)
    mer2 = pd.merge(mer,stop_times , how='inner', on='trip_id', left_on=None, right_on=None,
        left_index=False, right_index=False, sort=True)
    mer3 = pd.merge(mer2,stops , how='inner', on='stop_id', left_on=None, right_on=None,
        left_index=False, right_index=False, sort=True)
    mer4 = pd.merge(mer3,calendar , how='inner', on='service_id', left_on=None, right_on=None,
        left_index=False, right_index=False, sort=True)
    return mer4




def read_data():
    routes  = pd.read_csv("routes.txt",delimiter=",")
    trips = pd.read_csv("trips.txt",delimiter=",")
    stop_times = pd.read_csv("stop_times.txt",delimiter=",")
    stops = pd.read_csv("stops.txt",delimiter=",")
    calendar = pd.read_csv("calendar.txt", delimiter = ",")
    return(routes, trips, stop_times, stops, calendar)