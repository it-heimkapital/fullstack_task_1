from flask import jsonify
from flask_cors import CORS
from api import app


# To enables CORS support on all routes
CORS(app, resources={r"/*": {"origins": "*"}})


@app.route("/", methods=["GET"])
def default_route():
    return jsonify({"Message": "Backend is up and running"}), 200
