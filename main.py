import os
import sqlalchemy
import numpy
from flask import Flask

# app = Flask(__name__)


# @app.route("/")
# def hello_world():
#     return "Yep!"


# @app.route("/hello")
# def hello():
#     return "hello"

# if __name__ == "__main__":
#     app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
from flask import Flask, jsonify
import psycopg2
app = Flask(__name__)

# Connect to the PostgreSQL database
pg_connect_dict = {
    'dbname' : 'lab0',
    'user' : 'postgres',
    'password' : 'MonsterKitty3232',
    'host' : '34.133.237.115'
}

conn = psycopg2.connect(**pg_connect_dict) #unpack the dict above in the correct format

#define the decorators
@app.route('/') #python decorator
def hello_world(): #function that app.route decorator references
  response = hello()
  return response

def hello():
  return "hello, world"

#define another decorator
@app.route('/geojson', methods=['POST', 'GET'])
def get_geojson():
    # Execute a query to retrieve the polygon from the database
    cursor = conn.cursor()
    cursor.execute("SELECT ST_AsGeoJSON(new_polygon.*) FROM new_polygon;")
    result = cursor.fetchall()
    return result[0][0]
    
    if result is None:
        return jsonify({'error': 'Polygon not found'}), 404
    else:
        return jsonify({'geojson': result[0]})
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
