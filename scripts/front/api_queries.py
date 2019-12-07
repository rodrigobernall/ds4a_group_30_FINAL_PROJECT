import pandas as pd
import requests
import flask
import json
from pandas.io.json import json_normalize

def get_rows(str_query=None):
    response = requests.post("http://ec2-3-133-150-215.us-east-2.compute.amazonaws.com:8020/raw_query", json={"raw_query": str_query})
    return response.json()

test_query = "select * from view_ocupados_desocupados limit 10"

print(test_query)


print(get_rows(test_query))