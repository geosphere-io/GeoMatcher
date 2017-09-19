import psycopg2
import re

proposalTable = """CREATE TABLE IF NOT EXISTS proposal_items (
    action varchar(20),
    type varchar (255),
    category varchar(20),
    description varchar(2000),
    street1name varchar(60),
    street1type varchar(20),
    street2name varchar(60),
    street2type varchar(20)
    );
    SELECT AddGeometryColumn('proposal_items', 'the_geom',4326,'POINT',2);"""
alertTable = """CREATE TABLE IF NOT EXISTS alert_profiles (
    name varchar(255),
    requestlat double precision,
    requestlong double precision,
    radius double precision
);
SELECT AddGeometryColumn('alert_profiles', 'the_geom',4326,'POINT',2);"""

conn = psycopg2.connect(dbname="engr", user="engr",password="engr")
curs = conn.cursor()
curs.execute(proposalTable)
curs.execute(alertTable)
conn.commit()
