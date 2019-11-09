import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
import dash_table
from sqlalchemy import create_engine
import os
import flask
import requests
import json
from pandas.io.json import json_normalize


def download_dict_api(dict_name=None):
	r =requests.get('http://18.221.120.194:8020/factors/'+dict_name)
	print(r.json())
	r = pd.DataFrame.from_dict(r.json()['data']['topics'])
	index_col_name = r.columns[0]
	r = r.set_index(index_col_name)
	return r

marital_status = download_dict_api(dict_name='marital_dict')
sex = download_dict_api(dict_name='sex_dict')
print(sex)

## Definition of the elements of our dashboard
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

title = html.H2(children="¿Cuántos como yo?", className='h2-title')
title_div = html.Div(children=[title,],className='study-browser-banner row')



def create_radio_selector(sel_id=None, pandas_series=None):
	radio_selector = dcc.RadioItems(
		id=sel_id, 
		options=[{'label': value, 'value': index} for index, value in pandas_series.items()],
		labelStyle={'display': 'inline-block'}	
		)
	return radio_selector


def create_dropdown_selector(sel_id=None, pandas_series=None):
	dropdown_selector = dcc.Dropdown(
		id=sel_id, 
		options=[{'label': value, 'value': index} for index, value in pandas_series.items()],
		)
	return dropdown_selector


marital_select = create_dropdown_selector(sel_id='marital-select', pandas_series=marital_status['marital_status'])
sex_select = create_dropdown_selector(sel_id='sex-select', pandas_series=sex['sex_code'])

app.layout = html.Div(
	children=[title_div,
		html.Div(
			children=[html.H6("Estado civil",), marital_select]
		),
		html.Div(
			children=[html.H6("Sexo",), sex_select]
		)
		]
	)

if __name__ == "__main__":
    app.run_server(debug=True, host='0.0.0.0')
