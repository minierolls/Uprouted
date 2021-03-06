import requests
import json
import polyline
import random
import geojson

api_key = ""

def getDirections(origin, dest, mode):
    r = requests.post("https://maps.googleapis.com/maps/api/directions/json?origin={}&destination={}&key={}&mode={}".format(origin, dest, api_key, mode)).json()
    route = r["routes"][random.randint(0, len(r["routes"])-1)]
    distance = 0
    time = 0
    coord_list = []
    for leg in route["legs"][:1]:
        distance += leg["distance"]["value"]
        time += leg["duration"]["value"]
        for step in leg["steps"]:
            line = polyline.decode(step["polyline"]["points"], geojson=True)
            coord_list += line
    #geojson_line = geojson.LineString(coord_list)

    # distance in meters, time in seconds
    return (distance, time, coord_list)

def getRoute(distance, mode, destination="Return", origin="Current Location"):

    distance = distance * 1600 # convert to meters
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
    threshold = 1.1
    while True:
        if len(visited) == len(nearby_r["results"]):
            threshold *= 1.1
            visited = []
            places = []
            coord_list = []
            curr_dist = 0
            curr_time = 0
        res_num = random.randint(0, len(nearby_r["results"])-1)
        while res_num in visited:
            res_num = random.randint(0, len(nearby_r["results"])-1)
        place = nearby_r["results"][res_num]
        visited.append(res_num)
        places.append(place["name"])
        dest = place["place_id"]
        if start_placeid:
            (dist, time, coords) = getDirections("place_id:"+start, "place_id:"+dest, mode)
        else:
            (dist, time, coords) = getDirections(start, "place_id:"+dest, mode)
        if curr_dist + dist < distance * threshold:
            coord_list += coords
            curr_dist += dist
            curr_time += time
            if start_placeid:
                (distback, timeback, coordsback) = getDirections("place_id:"+dest, returnloc, mode)
                overlap = len(set(coord_list).intersection(set(coordsback)))/len(coordsback)
                if curr_dist + distback >= distance / threshold and overlap < 0.7 and curr_dist + distback <= distance * threshold:
                    curr_dist += distback
                    curr_time += timeback
                    coord_list += coordsback
                    break
        start = dest
        start_placeid = True
    coord_list = geojson.LineString(coord_list)
    curr_dist /= 1600
    time /= 60
    
    print(curr_dist, time, places, threshold)
        

if __name__ == '__main__':
    getRoute(3, "walking", origin="6231 Penn Ave Pittsburgh PA 15206")