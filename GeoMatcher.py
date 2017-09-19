
import psycopg2
import re
import sys
def metersToFeet(meters):
    return meters*3.2808;
class GeoMatcher:
    """Notifies when two columns from postgres have matching geometries."""
    def __init__(self):
        self.conn = psycopg2.connect(dbname="engr", user="engr",password="engr")
        self.conn.autocommit = True;

    def match(self,point1, point2,radius):
        cursor = self.conn.cursor()
        pointsql1 = "ST_SetSRID(ST_Point({0},{1}),4326)".format(point1[0],point1[1])
        pointsql2="ST_SetSRID(ST_Point({0},{1}),4326)".format(point2[0],point2[1])
        sql = "SELECT ST_distance({0},{1}::geography)".format(pointsql1,pointsql2);
        cursor.execute(sql)
        res2 = cursor.fetchall()[0][0]
        res2 = metersToFeet(res2)
        if(res2 < radius):
            return true;
        else:
            return false

    def checkForAlerts(self, name):
        print("Alerts for "+name);
        curs = self.conn.cursor()
        sql = "SELECT a.action, a.type, a.description, ST_distance(a.the_geom,b.the_geom::geography)<b.radius FROM proposal_items a, alert_profiles b where b.name = '{0}';".format(name)
        curs.execute(sql);
        res = curs.fetchall()
        for row in res:
            if(row[3]):
                print("{0} : {1} : {2}".format(row[0],row[1],row[2]))
    def checkForAlertsWithCategory(self, name, category):
        print("Alerts for "+name);
        curs = self.conn.cursor()
        sql = "SELECT a.action, a.type, a.description, ST_distance(a.the_geom,b.the_geom::geography)<b.radius FROM proposal_items a, alert_profiles b where b.name = '{0}' AND a.category='{1}';".format(name,category)
        curs.execute(sql);
        res = curs.fetchall()
        for row in res:
            if(row[3]):
                print("{0} : {1} : {2}".format(row[0],row[1],row[2]))
GeoMatcher().checkForAlerts("Ido Shoshani")
GeoMatcher().checkForAlertsWithCategory("Ido Shoshani","Parking")
