import json
import geojson
o = {
    "coordinates":[[[0, 0],[0.5,0],[0,0.5],[0,0]]],
    "type":"Polygon"
}
s = json.dumps(o)
gson = geojson.loads(s)
print(gson)
