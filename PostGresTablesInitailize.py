import psycopg2
import re
agendaTable = """CREATE TABLE IF NOT EXISTS proposal_agendas(
    agendaID SERIAL PRIMARY KEY,
    Post_date Date,
    meeting_date Date
    );
"""
proposalTable = """CREATE TABLE IF NOT EXISTS proposal_items (
    agendaID int references proposal_agendas(agendaID),
    itemID SERIAL PRIMARY KEY,
    action varchar(20),
    type varchar (255),
    category varchar(20),
    description varchar(2000)
    );

    SELECT AddGeographyColumn('proposal_items', 'the_geom',4326,'MULTIPOLYGON',2);
    """
UserTables = """CREATE TABLE IF NOT EXISTS alert_users(
    userID SERIAL PRIMARY KEY,
    name varchar(60),
    address varchar(255)
);
"""
alertTable = """CREATE TABLE IF NOT EXISTS alert_profiles (
    userID int references alert_users(userID),
    alertID SERIAL PRIMARY KEY,
    address varchar(255)
);
SELECT AddGeographyColumn('alert_profiles', 'the_geom',4326,'POLYGON',2);"""

conn = psycopg2.connect(dbname="engr", user="engr",password="engr")
curs = conn.cursor()
curs.execute(agendaTable)
curs.execute(proposalTable)
curs.execute(UserTables)
curs.execute(alertTable)
conn.commit()
