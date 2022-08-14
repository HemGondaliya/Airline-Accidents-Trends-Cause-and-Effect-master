import json
from flask import Flask
from flask import request, jsonify
from flask_cors import CORS, cross_origin
import numpy as np
import pandas as pd

app = Flask(__name__, static_folder='./')
cors = CORS(app)


@app.route("/getHeatMapData", methods=["GET"])
@cross_origin()
def getHeatMapData():
    with open('aviation_data_heat_map_count.json', 'r') as f:
        df = json.load(f)
    return df


@app.route("/getEventCountData", methods=["GET"])
@cross_origin()
def getEventData():
    with open('aviation_data_event_count.json', 'r') as f:
        df = json.load(f)
    return df


@app.route("/getClusterData", methods=["GET"])
@cross_origin()
def getClusterData():
    with open('cluster_data.json', 'r') as f:
        df = json.load(f)
    return df


if __name__ == "__main__":
    app.run(debug=True)
