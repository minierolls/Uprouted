# This file serves as the launch point for the backend,
# and will run the main server in a loop listening for
# requests at certain routes.

from flask import Flask, request
from flask_cors import CORS
import getroute as getroute

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

app = Flask(__name__)
CORS(app)

# Modify these before deployment
project_id = ''
service_account_json = ''

cred = credentials.Certificate(service_account_json)
firebase_admin.initialize_app(cred)

db = firestore.client()

@app.route('/getroute/<int:distance>/<string:mode>/<string:destination>/<string:origin>', methods=['GET'])
def get_route(distance, mode, destination, origin):
    (curr_dist, curr_time, coord_list) = getroute.getRoute(distance, mode, destination, origin)
    return {
            'estimated_distance': curr_dist,
            'estimated_time': curr_time,
            'route': coord_list,
    }


@app.route('/saveroute', methods=['POST'])
def save_route():
    user_ref = db.collection('users').document(request.user)
    history_ref = user_ref.collection('history')
    history_ref.add({
        'name': request.name,
        'route': request.geojson,
        'estimated_distance': request.estimated_distance,
        'estimated_time': request.estimated_time,
    })
    return

@app.route('/loadhistory/<string:user_name>', methods=['GET'])
def load_history(user_name):
    history = []
    users_ref = db.collection('users')
    user_ref = users_ref.document(user_name)
    user = user_ref.get()
    if user.exists:
        history_ref = user_ref.collection('history')
        for route in history_ref.stream():
            history.append(route)
    return {
            'history': history
    };
