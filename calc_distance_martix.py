import openrouteservice
from openrouteservice.directions import directions
import pandas as pd
import pickle

mapsClient1 = openrouteservice.Client(key="5b3ce3597851110001cf6248158b5f937ca741f19989772eca0fa33b")
mapsClient2 = openrouteservice.Client(key="5b3ce3597851110001cf62483db75e8b14fc4f57bbc0b1405b3dc178")
mapsClient3 = openrouteservice.Client(key="5b3ce3597851110001cf624862f399781c994dd0bce468fd7367c747")
mapsClient4 = openrouteservice.Client(key="5b3ce3597851110001cf6248e932de7a669c4527bb0f393bede48cb4")

def getVals(response):
	row = response['routes'][0]['summary']
	try :
		distance,time = row['distance'],row['duration']
	except :
		return "NA","NA"
	return distance,time

def distance_matrix(rownumber, destinations,origin):
	distances = []
mapsClient = mapsClient1
if(rownumber%4==1):
	mapsClient = mapsClient2
if(rownumber%4==2):
	mapsClient = mapsClient3
if(rownumber%4==3):
	mapsClient = mapsClient4
	print("hello")
	for value in destinations:
		coords = (origin,value)
		print(coords)
		response = mapsClient.directions(coords)
		distance,time = getVals(response)
		distances.append(distance)
	return distances

ward_input = "Data/circle_coords.csv"
labs_input = "Data/labs.csv"
df = pd.read_csv(ward_input)
df_labs = pd.read_csv(labs_input)
distances = [["Name"]]
destinations = []
for row in df.iterrows():
	row = row[1]
	destinations.append((row['Longitude'],row['Latitude']))
	distances[0].append(row["Circle"])

rownumber = 1
for row in df_labs.iterrows():
	row = row[1]
	print(row)
	distances.append([row['Testing ceter']])
	print((row['Longitude'],row['Latitude']))
	partial_distances = distance_matrix(rownumber, destinations,(row['Longitude'],row['Latitude']))
	for dist in partial_distances:
		distances[rownumber].append(dist)
	rownumber += 1

filename = "distance_matrix"
with open(filename,'wb') as f:
	pickle.dump(distances,f)