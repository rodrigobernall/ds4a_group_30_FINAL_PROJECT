import pandas as pd
import requests
import flask
import json
from pandas.io.json import json_normalize

def get_rows(str_query=None):
    response = requests.post("http://ec2-3-133-150-215.us-east-2.compute.amazonaws.com:8020/employement_rate", data = str_query)
    return response.json()

test_query = {"month":1,"gender":"Hombre","municipio":76,"age_base": 23,"age_top":35,"marital_status":"Esta soltero (a)","aggregator":"nivel_educ"}

print(test_query)


print(get_rows(test_query))