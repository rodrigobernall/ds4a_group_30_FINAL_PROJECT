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
	# r =requests.get('http://18.221.120.194:8020/factors/'+dict_name)
	# print(r.json())
	# r = pd.DataFrame.from_dict(r.json()['data']['topics'])
	# index_col_name = r.columns[0]
	# r = r.set_index(index_col_name)
	# return r
	return series_name

## Definition of the elements of our dashboard
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


title = html.H2(children="¿Cuántos como yo?", className='h2-title')
title_div = html.Div(children=[title,],className='study-browser-banner row')

token = 'pk.eyJ1IjoibmV3dXNlcmZvcmV2ZXIiLCJhIjoiY2o2M3d1dTZiMGZobzMzbnp2Z2NiN3lmdyJ9.cQFKe3F3ovbfxTsM9E0ZSQ'
with open('data.json') as f:
    geojson = json.loads(f.read())


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
),

html.Div(
                        dcc.Graph(
                            id='map-plot',
                            figure={ 
                                'data': [go.Choroplethmapbox(
                                    geojson=geojson,
                                    locations=df['ID_MUNICIPIO'],
                                    z=df['ID_MUNICIPIO'],
                                    colorscale='Viridis',
                                    text=df['NOMBRE_MPI'],
                                    colorbar_title="Prueba"
                                )],
                                'layout': go.Layout(
                                        mapbox_style="dark",
                                        mapbox_accesstoken=token,
                                        mapbox_zoom=3,
                                        margin={'t': 0, 'l': 0, 'r': 0, 'b': 0},
                                        mapbox_center={"lat": 4.6482837, "lon": -74.2478922}
                                    )
                            }
                        ),
                    ),

])



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
