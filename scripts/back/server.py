
from flask import Flask, request, jsonify
import pandas as pd
import joblib
import os
import models.filter_model as process


app = Flask(__name__)



@app.route('/municipios', methods=['GET'])
def retrieve_municipios():
    municipios = process.table_builder("municipalities")
    return {
        'status': 'OK',
        'data': municipios.to_dict()
    }

@app.route('/departamentos', methods=['GET'])
def retrieve_departamentos():
    municipios = process.table_builder("departments")
    return {
        'status': 'OK',
        'data': municipios.to_dict()
    }

@app.route('/factors/<table>', methods=['GET'])
def retrieve_factors(table):
    factors = process.table_builder(table)
    return {
        'status': 'OK',
        'data': {
            'topics': factors.to_dict()
        }
    }


@app.route('/status', methods=["GET"])
def status():
    return jsonify({"message": "ok"})


app.run(host='0.0.0.0', port=8020, debug=False )