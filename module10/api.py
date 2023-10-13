import json

from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_socketio import SocketIO

from pymongo import MongoClient
from rest_utility.utils import extract_customer_from_request_body

# region rest api: configuration
crm_rest_api = Flask(__name__)
crm_rest_api.config["DEBUG"] = True
cors = CORS(crm_rest_api)
socketio = SocketIO(crm_rest_api, cors_allowed_origins="*")
# endregion

# region pymongo configuration
mongo_client = MongoClient("mongodb://localhost:27017")
siemens_database = mongo_client["siemens_crm"]
customers = siemens_database.customers
# endregion

# region rest api: validation
customer_fields = [
    "identity", "fullname", "photo", "birthYear",
    "gsm", "email", "active", "address"
]


# endregion

# region rest api: get methods
@crm_rest_api.route("/crm/api/v1/customers/<identity>", methods=["GET"])
def get_customer_by_id(identity: str):
    return jsonify(customers.find_one({"_id": identity}))


@crm_rest_api.route("/crm/api/v1/customers", methods=["GET"])
def get_customers():
    return json.dumps([cust for cust in customers.find({})])


# endregion

# region rest api: post/put/patch/delete methods
@crm_rest_api.route("/crm/api/v1/customers", methods=["POST"])
def acquire_customer():
    customer = extract_customer_from_request_body(request, customer_fields)
    customers.insert_one(customer)
    socketio.emit('acquire', customer)
    return jsonify({"status": "ok"})


@crm_rest_api.route("/crm/api/v1/customers/<identity>", methods=["PUT", "PATCH"])
def update_customer(identity: str):
    customer = extract_customer_from_request_body(request, customer_fields)
    customers.find_one_and_update(
        {"_id": identity},
        {"$set": customer},
        upsert=False
    )
    return jsonify({"status": "ok"})


@crm_rest_api.route("/crm/api/v1/customers/<identity>", methods=["DELETE"])
def release_customer_by_id(identity: str):
    customer = customers.find_one({"_id": identity})
    customers.delete_one({"_id": identity})
    socketio.emit('release', customer)
    return jsonify(customer)


# endregion

socketio.run(crm_rest_api, port=7001)
