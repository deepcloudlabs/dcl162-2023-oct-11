"""
mongodb
pymongo configuration
"""
import json

from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_socketio import SocketIO
from pymongo import MongoClient

from hr.utility import extract_employee_from_request

mongo_client = MongoClient("mongodb://localhost:27017")
hr_db = mongo_client["hrdb"]
employees = hr_db.employees

api = Flask(__name__)
api.config["DEBUG"] = True
cors = CORS(api)
socketio = SocketIO(api, cors_allowed_origins="*")

fields = [
    "identity", "fullname", "iban", "photo", "salary",
    "birthYear", "department", "fulltime"
]


@api.route("/hr/api/v1/employees/<identity>", methods=["GET"])
def get_employee_by_identity(identity):
    return jsonify(employees.find_one({"_id": identity}))


@api.route("/hr/api/v1/employees", methods=["GET"])
def get_employees():
    return json.dumps([emp for emp in employees.find({})])


@api.route("/hr/api/v1/employees", methods=["POST"])
def add_employee():
    employee = extract_employee_from_request(request, fields)
    employees.insert_one(employee)
    socketio.emit('hire', employee)
    return jsonify({"status": "ok"})


@api.route("/hr/api/v1/employees/<identity>", methods=["PUT", "PATCH"])
def update_employee(identity):
    employee = extract_employee_from_request(request, fields)
    employees.find_one_and_update(
        {"_id": identity},
        {"$set": employee},
        upsert=False
    )
    return jsonify({"status": "ok"})


@api.route("/hr/api/v1/employees/<identity>", methods=["DELETE"])
def remove_employee(identity):
    employee = employees.find_one({"_id": identity})
    employees.delete_one({"_id": identity})
    socketio.emit('fire', employee)
    return jsonify(employee)


socketio.run(api, port=7001)
