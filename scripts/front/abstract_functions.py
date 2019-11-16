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



df = pd.read_csv('Chile.csv')

def fetch_series(series_name):
	series_name = df[series_name]   # Temporal. Viene de la API
	return series_name

## Definition of the elements of our dashboard
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

title = html.H2(children="¿Cuántos como yo?", className='h2-title')
title_div = html.Div(children=[title,],className='study-browser-banner row')

histogram_x_select = dcc.Dropdown(
    id="histogram-x-select",
    options=[{'label': label, 'value': label} for label in df.columns],
    value='income'
)
	

app.layout = html.Div(children=[
	title_div,
	html.H6("Seleccione X para el histograma",), histogram_x_select,
    html.Div(
		dcc.Graph(id='histogram',
		figure={}
		)
)])



@app.callback(
    dash.dependencies.Output('histogram', 'figure'),
    (
        dash.dependencies.Input('histogram-x-select', 'value'),
    )
)

def update_histogram(x_name):
    series_x = fetch_series(x_name)
    return {'data': 
				[{
				'x': series_x,
				'type': 'histogram'
					},],
			'layout': {'title': 'Histograma de {}'.format(x_name),}
			}


if __name__ == "__main__":
    app.run_server(debug=True)
