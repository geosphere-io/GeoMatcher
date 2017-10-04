from flask import Flask
from flask import request
import json
import geojson
import GeoMatcher;
from shapely.geometry import shape
app = Flask(__name__)
geo = GeoMatcher.GeoMatcher()
##App to run alongside front-end
@app.route('/CheckShape',methods = ['GET','POST'])
def CheckShape():
    #Todo
    #arguments:  geojson
    #returns : JSon list of items
    error = None;
    geom = geojson.loads(request.form['geometry'])
    res = geo.checkAgainstShape(geom)
    dicts = []
    for row in res:
        dicts.append({"Action":row[0],"Object":row[1],"Description":row[2]})
    return json.dumps(dicts)
@app.route('/AddUser', methods = ['POST'])
def AddUser():
    #Todo
    #arguments : username and email
    #returns : "saved", posts to backend
    error = None;
    name = request.form['username']
    address = request.form['email']
    res= geo.AddUser(name,address)
    return str(res[0])
@app.route('/AddAlert', methods = ['POST'])
def AddAlert():

    error = None;
    id = request.form['userId']
    area = geojson.loads(request.form['area'])
    return geo.AddAlertProfile(id,area)
