
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

@app.route('/filtered_table', methods=['POST'])
def filtered_table():
    payload = request.json
    print(payload)
    filters = process.filter_builder(payload["filters"])
    print(filters)
    data = process.table_builder(payload["table"],  filters)
    if data.empty==False:
        info_tabla = data.to_dict()


    else:
        info_tabla = "no info"

    obj = {
        'status': 'OK',
        'data': {
            'table':info_tabla
        }
    }
    return jsonify(obj)

@app.route('/agg_pct', methods=['POST'])
def agg_table():
    payload = request.json
    data = process.agg_builder_percent(payload["tabla"], payload["var_agg"], payload["agregador"])
    if data.empty==False:
        info_tabla = data.to_dict()


    else:
        info_tabla = "no info"

    obj = {
        'status': 'OK',
        'data': {
            'table':info_tabla
        }
    }
    return jsonify(obj)


@app.route('/raw_query', methods=['POST'])
def raw_query():
    payload = request.json
    data = process.table_query(payload["raw_query"])
    if data.empty==False:
        info_tabla = data.to_dict()


    else:
        info_tabla = "no info"

    obj = {
        'status': 'OK',
        'data': {
            'table':info_tabla
        }
    }
    return jsonify(obj)

@app.route('/status', methods=["GET"])
def status():
    return jsonify({"message": "ok"})


app.run(host='0.0.0.0', port=8020, debug=False )
