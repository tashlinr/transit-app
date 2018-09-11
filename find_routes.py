# import pandas library for data manipulation 
import pandas as pd


#read in txt files needed
routes  = pd.read_csv("routes.txt",delimiter=",")
trips = pd.read_csv("trips.txt",delimiter=",")
stop_times = pd.read_csv("stop_times.txt",delimiter=",")
stops = pd.read_csv("stops.txt",delimiter=",")



#Merge the files
#Goal is to connect Routes(route_ids) to Stops(stop_name)


#first merge routes and trip ON route_id
mer = pd.merge(routes, trips, how='inner', on='route_id', left_on=None, right_on=None,
left_index=False, right_index=False, sort=True)

#Second merge new table with stop_times ON trip_id from the trip table
mer2 = pd.merge(mer,stop_times , how='inner', on='trip_id', left_on=None, right_on=None,
left_index=False, right_index=False, sort=True)

# Third merge new table with stops ON stop_id from stop_times table
mer3 = pd.merge(mer2,stops , how='inner', on='stop_id', left_on=None, right_on=None,
left_index=False, right_index=False, sort=True)



# Now we have a table with the routes, trips, stop_times, and stops all together.
# We can filter stop_names for "Grand Cental" as explicitly asked. 
routes_gc = mer3[mer3['stop_name'].str.contains("Grand Central", na=False)]

#Last output a list of the unique route ids that pass through Grand Central.
output = list(routes_gc['route_id'].unique())

#Using pythons built in sort method to improve readability
output.sort()

print("Route IDs passing through Grand Central: \n{}".format(output))