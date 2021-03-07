import requests
import json
import polyline
import random
import geojson

api_key = "AIzaSyCTj8Nu-6coDK1WpYGcoKJ9P0FfYKDYXHU"

def getDirections(origin, dest, mode):
    r = requests.post("https://maps.googleapis.com/maps/api/directions/json?origin={}&destination={}&key={}&mode={}".format(origin, dest, api_key, mode)).json()
    route = r["routes"][random.randint(0, len(r["routes"])-1)]
    distance = 0
    time = 0
    coord_list = []
    for leg in route["legs"][:1]:
        distance += leg["distance"]["value"]
        time += int(leg["duration"]["value"])
        for step in leg["steps"]:
            line = polyline.decode(step["polyline"]["points"], geojson=True)
            coord_list += line

    # distance in meters, time in seconds
    return (distance, time, coord_list)

def getRoute(distance, mode, destination="Return", origin="Current Location"):

    distance = distance * 1000 # convert to meters
    radius = distance / 2
    coord_list = []
    curr_dist = 0
    curr_time = 0

    if origin == "Current Location":
        geo_r = requests.post("https://www.googleapis.com/geolocation/v1/geolocate?key={}".format(api_key)).json()
        latitude = geo_r["location"]["lat"]
        longitude = geo_r["location"]["lng"]
    else:
        place = "%".join(origin.split())
        place_r = requests.post("https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input={}&inputtype=textquery&fields=geometry&key={}".format(place, api_key)).json()
        loc = place_r["candidates"][0]["geometry"]["location"]
        latitude = loc["lat"]
        longitude = loc["lng"]

    if destination == "Return":
        returnloc = str(latitude)+","+str(longitude)
    else:
        retplace = "%".join(destination.split())
        retplace_r = requests.post("https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input={}&inputtype=textquery&fields=geometry&key={}".format(retplace, api_key)).json()
        retloc = retplace_r["candidates"][0]["geometry"]["location"]
        retlatitude = loc["lat"]
        retlongitude = loc["lng"]
        returnloc = str(retlatitude)+","+str(retlongitude)

    nearby_r = requests.post("https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={},{}&radius={}&key={}".format(latitude, longitude, str(radius), api_key)).json()

    # Finding directions to nearby places
    start = str(latitude)+","+str(longitude)
    start_placeid = False 
    visited = []
    places = []
    success = True 
    threshold = 1.1
    for r in nearby_r["results"]:
        if r["name"] == "UPMC Shadyside":
            first_place = r["place_id"]
        if r["name"] == "Stephen Foster Memorial":
            second_place = r["place_id"]
        
    if start_placeid:
        (dist, time, coords) = getDirections("place_id:"+start, "place_id:"+first_place, mode)
    else:
        (dist, time, coords) = getDirections(start, "place_id:"+first_place, mode)
    coord_list += coords
    curr_dist += dist
    curr_time += time

    (dist, time, coords) = getDirections("place_id:"+first_place, "place_id:"+second_place, mode)
    coord_list += coords
    curr_dist += dist
    curr_time += time

    (distback, timeback, coordsback) = getDirections("place_id:"+second_place, returnloc, mode)
    curr_dist += distback
    curr_time += timeback
    coord_list += coordsback

    coord_list = geojson.LineString(coord_list)
    curr_dist /= 1000
    curr_time /= 60
    print(curr_dist, curr_time, coord_list)
    return (curr_dist, curr_time, coord_list)


if __name__ == '__main__':
    getRoute(5, "walking", origin="carnegie mellon university")
