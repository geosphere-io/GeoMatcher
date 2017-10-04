
import psycopg2
import re
import sys
from shapely.geometry import shape
import geojson
import json

def metersToFeet(meters):
    return meters*3.2808;
class GeoMatcher:
    """Notifies when two columns from postgres have matching geometries."""
    def __init__(self):
        self.conn = psycopg2.connect(dbname="engr", user="engr",password="engr")
        self.conn.autocommit = True;

    ##Run User against Points
    def checkAgainstShape(self, geojs):
        cursor = self.conn.cursor()
        shp = shape(geojs);
        shapesql = "ST_GeomFromText('{0}')".format(shp.wkt)
        sql = "SELECT a.action, a.type, a.description From proposal_items a Where ST_INTERSECTS(a.the_geom,{0})".format(shapesql)
        cursor.execute(sql)
        res = cursor.fetchall()
        return res

    def UsercheckForAlerts(self, name):
        print("Alerts for "+name);
        curs = self.conn.cursor()
        sql = "SELECT a.action, a.type, a.description, ST_INTERSECTS(a.the_geom,b.the_geom)<b.radius FROM proposal_items a, alert_profiles b where b.name = '{0}';".format(name)
        curs.execute(sql);
        res = curs.fetchall()
        for row in res:
            if(row[3]):
                print("{0} : {1} : {2}".format(row[0],row[1],row[2]))
    ##Run User against Points with Category

    def checkForAlertsWithCategory(self, name, category):
        print("Alerts for "+name);
        curs = self.conn.cursor()
        sql = "SELECT a.action, a.type, a.description, ST_distance(a.the_geom,b.the_geom::geography)<b.radius FROM proposal_items a, alert_profiles b where b.name = '{0}' AND a.category='{1}';".format(name,category)
        curs.execute(sql);
        res = curs.fetchall()
        for row in res:
            if(row[3]):
                print("{0} : {1} : {2}".format(row[0],row[1],row[2]))
    ## Run 1 Point against Users

    def checkForUsers(self, item):
        print("Alerting for "+item.object)
        sql = "Select "


    def AddUser(self,name,address):
        curs = self.conn.cursor()
        sql = "INSERT INTO alert_users(name,address) VALUES ('{0}','{1}') RETURNING userid;".format(name,address)
        curs.execute(sql)
        return curs.fetchone()
    def AddAlertProfile(self,id,geojsonArea):
        area = shape(geojsonArea)
        curs = self.conn.cursor()
        sql = "INSERT INTO alert_profiles(userID,the_geom) VALUES({0},ST_GeomFromText('{1}',4326));".format(id,area.wkt)
        print(sql)
        curs.execute(sql);
        return "saved";
