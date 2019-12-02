import importlib
import pathlib
import os

import pandas as pd
import numpy as np
from datetime import datetime as dt
import flask
import requests

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
from dash.dependencies import Input, Output, State
import json
from sqlalchemy import create_engine

#app = dash.Dash(__name__, external_stylesheets=['https://codepen.io/uditagarwal/pen/oNvwKNP.css'])
#app = dash.Dash(__name__, external_stylesheets=['https://github.com/plotly/dash-sample-apps/blob/master/apps/dash-oil-and-gas/assets/styles.css'])
app = dash.Dash(__name__, external_stylesheets=['https://cdn.rawgit.com/plotly/dash-app-stylesheets/2d266c578d2a6e8850ebce48fdb52759b2aef506/stylesheet-oil-and-gas.css'])
token = 'pk.eyJ1IjoibmV3dXNlcmZvcmV2ZXIiLCJhIjoiY2o2M3d1dTZiMGZobzMzbnp2Z2NiN3lmdyJ9.cQFKe3F3ovbfxTsM9E0ZSQ'

with open('Colombia_Transformado.json') as f:
    geojson = json.loads(f.read())

df_correc = pd.read_csv('df_colombia.csv')
df_correc['MPIOS'] = df_correc['MPIOS'].apply(lambda x: str(x))
df_correc['MPIOS'] = df_correc['MPIOS'].str.zfill(5)
df_correc['DPTO']=df_correc['DPTO'].apply(lambda x: '{0:0>3}'.format(x))
df_correc['MPIO']=df_correc['MPIO'].apply(lambda x: '{0:0>3}'.format(x))
df_correc['COD_DANE']=df_correc['DPTO'].astype(str)+df_correc['MPIO'].astype(str)


def download_dict_api(dict_name=None):
	r =requests.get('http://ec2-3-133-150-215.us-east-2.compute.amazonaws.com:8020/factors/'+dict_name)
	r = pd.DataFrame.from_dict(r.json()['data']['topics'])
	index_col_name = r.columns[0]
	r = r.set_index(index_col_name)
	return r

marital_status = download_dict_api(dict_name='marital_dict')
sex = download_dict_api(dict_name='sex_dict')
educational = download_dict_api(dict_name='education_dict')
print(sex)


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
sex_select = create_radio_selector(sel_id='sex-select', pandas_series=sex['sex_status'])
educational_select = create_dropdown_selector(sel_id='educational-select', pandas_series=educational['education_level'])


app.layout = html.Div(children=[
    html.Div(
        children=[
            html.Div(
                [
                html.Img(
                            src=app.get_asset_url("colombia.png"),
                            id="team30-image",
                            style={
                                "height": "150px",
                                "width": "auto",
                                "margin-bottom": "25px",
                            },
                        ),
                ],
                className="three columns center",
            ),
            html.Div(
                [
                html.H3(
                    "Cuántos Como Yo?",
                    style={"margin-bottom": "0px"},
                ),
                html.H5(
                    "Production Overview", style={"margin-top": "0px"}
                ),
                ],
                className="six columns",
            ),
            html.Div(
                [
                    html.Div(
                    [
                    html.Img(
                            src=app.get_asset_url("mintic.jpg"),
                            id="mintic-image",
                            style={
                                "height": "150px",
                                "width": "auto",
                                "margin-bottom": "25px",
                            },
                        ),
                    ],
                    ),
                    
                ],
                className="two columns",
            )
        ],
       
    ),
    html.Div(
        children=[
            html.Div(
                [
                   html.Div(
                    [
                        html.H6(
                            "Seleccione un mes:",
                            className="control_label",
                        ),
                        dcc.Dropdown(
                            id='month-dropdown',
                            options=[
                                {'label': 'Enero', 'value': '1'},
                                {'label': 'Febrero', 'value': '2'},
                                {'label': 'Marzo', 'value': '3'}
                            ],
                            value='1'
                        ),
                        html.Div(
                            children=[
                                    html.H6("Seleccione Municipio"),
                                    dcc.Dropdown(
                                        id="study-dropdown",
                                        multi=True,
                                        value=('SANTAFE DE BOGOTA D.C.',),
                                        options=[{'label': label, 'value': label} for label in df_correc['NOMBRE_MPI'].unique()]
                                    )
                                ]
                        ),
                        html.Div(
                            children=[
                                html.H6("Estado Civil:", className="control_label"), 
                                marital_select
                            ]
                        ),
                        html.Div(
                            children=[
                                html.H6("Género:", className="control_label"), 
                                sex_select
                            ]
                        ),
                        html.Div(
                            children=[
                                html.H6("Nivel Educativo:", className="control_label"), 
                                educational_select
                            ]
                        ),
                        
                    ],
                    id="cross-filter-options",
                ),
                ],
                className="pretty_container three columns",
            ),
            html.Div(
                [
                html.Div(
                    [
                       dcc.Graph(id="pie_graph4"),

                    ],
                    className="pretty_container",
                ),
                ],
                className="six columns",
            ),
            html.Div(
                [
                   html.Div(
                    [dcc.Graph(id="pie_graph2")],
                    className="pretty_container",
                ),
                ],
                className="three columns",
            )
        ],
       
    ),
    html.Div(
        children=[
            html.Div(
                [
                  html.Div(
                    [
                        html.H1(children="Mapa de Colombia", style={'textAlign': 'center'}),
                            dcc.Graph(id='map-plot', figure={ 
                            'data': [go.Choroplethmapbox()],
                            'layout': go.Layout(
                                    mapbox_style="dark",
                                    mapbox_accesstoken=token,
                                    mapbox_zoom=5,
                                    margin={'t': 0, 'l': 0, 'r': 0, 'b': 0},
                                    mapbox_center={"lat": 4.6109886, "lon": -74.072092}
                                )
                                }
                        )

                    ],
                    className="pretty_container",
                ),
                ],
                className="six columns center",
            ),
            html.Div(
                [
                    dcc.Graph(id="pie_graph3"),
                ],
                className="six columns",
            ),       
        ],
        
    )
])


def get_filtered_rows(municipios):
    data = df_correc[df_correc['NOMBRE_MPI'].isin(municipios)].copy()
    return data

def info_por_municipio(municipios):
    data =[]
    # print(municipios)
    df = get_filtered_rows(municipios)
    # print(df)
    data.append(go.Choroplethmapbox(
                geojson=geojson,
                locations=df['MPIOS'],
                z=df['HECTARES'],
                colorscale='earth',
                text=df['NOMBRE_MPI'],
                colorbar_title="HECTAREAS"
            ))
    # print(data)
    return data

@app.callback(
    dash.dependencies.Output('map-plot', 'figure'), # component with id map-plot will be changed, the 'figure' argument is updated
    [
        dash.dependencies.Input('study-dropdown', 'value'),
    ]
)
def actualizar_mapa(value):
    return { 
            'data': info_por_municipio(value),
            'layout': go.Layout(
                mapbox_style="open-street-map",
                mapbox_accesstoken=token,
                mapbox_zoom=6,
                margin={'t': 0, 'l': 0, 'r': 0, 'b': 0},
                mapbox_center={"lat": 4.6109886, "lon": -74.072092}
            )
        }


def get_rows(str_query=None):
    response = requests.post("http://ec2-3-133-150-215.us-east-2.compute.amazonaws.com:8020/raw_query", json={"raw_query":str_query})
    return response.json()

print(get_rows("select case when ap.p6020=1 then 'Hombre' else 'Mujer' end as Sexo, ap.p6040 as Anios_cumplidos from area_personas ap where mes=3 group by ap.p6040, ap.p6020"))


if __name__ == "__main__":
    app.run_server(debug=True)
