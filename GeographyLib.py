import geojson
import GeoMatcher
from shapely.geometry import shape

def geojson_to_wkt(geojson):
    geo = shape(geojson)
    return geo.wkt
