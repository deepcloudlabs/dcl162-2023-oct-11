from flask import Flask
from flask_cors import CORS
from flask_socketio import SocketIO

crm_rest_api = Flask(__name__)
crm_rest_api.config["DEBUG"] = True
cors = CORS(crm_rest_api)
SocketIO(crm_rest_api, cors_allowed_oigins="*")

from pymongo import MongoClient

mongo_client = MongoClient("mongodb://localhost:27017")
siemens_database = mongo_client["siemens_crm"]
customers = siemens_database.customers


@crm_rest_api.route("/crm/api/v1/customers/<identity>", methods=["GET"])
def get_customer_by_id(identity: str):
    return 
