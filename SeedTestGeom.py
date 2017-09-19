import psycopg2
import re
import sys

conn = psycopg2.connect(dbname="engr", user="engr",password="engr")
conn.autocommit = True;
#Action: ESTABLISH; Category: Parking; Object: RESIDENTIAL PERMIT PARKING AREA J, 2-HOUR PARKING, 8 AM TO 5  PM, MONDAY THROUGH FRIDAY, EXCEPT VEHICLES WITH AREA J PERMIT; description:11th Avenue, both sides, between Judah Street and Kirkham Street (1400 block) Points: -122.468190788 ,37.7602176497 Street: KIRKHAM,11TH Points: -122.468321006 ,37.7620811122 Street: 11TH,JUDAH
#Action: ESTABLISH; Category: Traffic; Object: STOP SIGNS; description:Balboa Street, eastbound and westbound, at 11th Avenue, making this intersection an all-way  STOP Points: -122.469361012 ,37.7769903264 Street: 11TH,BALBOA

Test_items  = [{"Action":"ESTABLISH","Catergory":"Parking","Object":"RESIDENTIAL PERMIT PARKING AREA J, 2-HOUR PARKING, 8 AM TO 5  PM, MONDAY THROUGH FRIDAY, EXCEPT VEHICLES WITH AREA J PERMIT","Description":"11th Avenue, both sides, between Judah Street and Kirkham Street (1400 block)","Geom":"ST_SetSRID(ST_Point(37.7602176497,-122.468190788),4326)"},
                {"Action":"ESTABLISH","Catergory":"Traffic","Object":"STOP SIGNS","Description":"Balboa Street, eastbound and westbound, at 11th Avenue, making this intersection an all-way","Geom":"ST_SetSRID(ST_Point(37.7769903264,-122.469361012),4326)"}]

Test_alerts = [{"Name":"Ido Shoshani","requestlat":37.7769903264,"requestlong":-122.469361012,"radius":10,"ST_SetSRID(ST_Point(37.7769903264,-122.469361012),4326)"}]
sql=""
for item in Test_items:
    sql += "INSERT INTO proposal_items(action, type, category, description,the_geom) VALUES ('{0}','{1}','{2}','{3}',{4}) RETURNING 'did';".format(item["Action"],item["Object"],item["Catergory"],item["Description"],item["Geom"])
for user in Test_alerts:
    sql += "INSERT INTO alert_profiles(name, requestlat, requestlong, radius,the_geom) VALUES ('{0}',{1}, {2}, {3}, {4}) RETURNING 'did';".format(user["Name"],user["requestlat"],user["requestlong"],user["radius"])

print(sql)
cur = conn.cursor()
cur.execute(sql)
res = cur.fetchone()
print(res[0])
