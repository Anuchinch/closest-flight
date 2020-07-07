import json, requests
from math import pi, radians
from geopy.distance import geodesic

r = requests.get("https://opensky-network.org/api/states/all")
response = r.json()

lat = radians(float(input("Enter latitude in degrees (positive for N, negative for S):")))
lon = radians(float(input("Enter longitude in degrees (positive for E, negative for W):")))
coord = (lat, lon)

closest_index = 0
closest_distance = 6378*2*pi

for i in range(0, len(response['states'])):
    flight = response['states'][i]
    f_lon, f_lat = flight[5], flight[6]
    if(f_lon != None and f_lat!= None):
        f_coord = (radians(f_lat), radians(f_lon))
        dist = geodesic(coord, f_coord)
        if(dist < closest_distance):
            closest_distance = dist
            closest_index = i

flight = response['states'][closest_index]
icao, callsign, country, f_lon, f_lat, f_alt = flight[0], flight[1], flight[2], flight[5], flight[6], flight[13]
print("Closest flight is:")
print("ICAO24 ID:", icao)
print("Callsign:", callsign)
print("Country of origin:", country)
print("Latitude:", f_lat, "Longitude:", f_lon, "Altitude:", f_alt)
print("Distance from given location:", closest_distance)
