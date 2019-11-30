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



def get_rows(str_query=None):
    response = requests.post("http://ec2-3-133-150-215.us-east-2.compute.amazonaws.com:8020/raw_query", json={"raw_query":str_query})
    return response.json()

test_json = get_rows("select ap.p6040 as \"Edad\", round(sum(fex_c_2011)) as \"Cantidad de personas\" from area_personas ap where mes=3 group by ap.p6040")

df = pd.DataFrame.from_dict(test_json['data']['table'])

print(df)

def fetch_series(series_name):
	series_name = df[series_name] 
	return series_name

## Definition of the elements of our dashboard
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


title = html.H2(children="¿Cuántos como yo?", className='h2-title')
title_div = html.Div(children=[title,],className='study-browser-banner row')



histogram_x_select = dcc.Dropdown(
    id="histogram-x-select",
    options=[{'label': label, 'value': label} for label in df.columns],
)

barplot_x_select = dcc.Dropdown(
    id="barplot-x-select",
    options=[{'label': label, 'value': label} for label in df.columns],
)

barplot_y_select = dcc.Dropdown(
    id="barplot-y-select",
    options=[{'label': label, 'value': label} for label in df.columns],
)
	

app.layout = html.Div(children=[
	title_div,
	html.H6("Seleccione X para el histograma",), histogram_x_select,
    html.Div(
		dcc.Graph(id='histogram',
		figure={})
	),

	html.H6("Seleccione X y Y para el diagrama de barras",), barplot_x_select, barplot_y_select,
    html.Div(
		dcc.Graph(id='barplot',
		figure={})
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





@app.callback(
    dash.dependencies.Output('barplot', 'figure'),
    (
        dash.dependencies.Input('barplot-x-select', 'value'),
        dash.dependencies.Input('barplot-y-select', 'value'),
    )
)

def update_barplot(x_name, y_name):
    series_x = fetch_series(x_name)
    series_y = fetch_series(y_name)
    
    series_plot = go.Bar(x=series_x, y=series_y )
    return {'data': 
				[series_plot],
			'layout': {'title': 'Diagrama de barras de {} y {}'.format(x_name, y_name),}
			}

if __name__ == "__main__":
    app.run_server(debug=True)
