import openrouteservice
from openrouteservice.directions import directions

mapsClient = openrouteservice.Client(key="5b3ce3597851110001cf6248158b5f937ca741f19989772eca0fa33b")

def getVals(response):
	row = response['routes'][0]['summary']
	try :
		distance,time = row['distance'],row['duration']
	except :
		return "NA","NA"
	return distance,time

def distance_matrix(origin,destinations):
	distances = {}
	for (key,value) in destinations.items():
		coords = (origin,value.coord)
		response = mapsClient.directions(coords)
		distance,time = getVals(response)
		distances[key] = distance
	return distances