import pandas as pd
import dash
import dash_html_components as html
import dash_core_components as dcc
import plotly.graph_objects as go
from dash.dependencies import Input, Output
import json

app = dash.Dash(__name__, external_stylesheets=['https://codepen.io/uditagarwal/pen/oNvwKNP.css'])
token = 'pk.eyJ1IjoibmV3dXNlcmZvcmV2ZXIiLCJhIjoiY2o2M3d1dTZiMGZobzMzbnp2Z2NiN3lmdyJ9.cQFKe3F3ovbfxTsM9E0ZSQ'
with open('Colombia_Transformado.json') as f:
    geojson = json.loads(f.read())

df_correc = pd.read_csv('df_colombia.csv')
df_correc['MPIOS'] = df_correc['MPIOS'].apply(lambda x: str(x))
df_correc['MPIOS'] = df_correc['MPIOS'].str.zfill(5)
df_correc['DPTO']=df_correc['DPTO'].apply(lambda x: '{0:0>3}'.format(x))
df_correc['MPIO']=df_correc['MPIO'].apply(lambda x: '{0:0>3}'.format(x))
df_correc['COD_DANE']=df_correc['DPTO'].astype(str)+df_correc['MPIO'].astype(str)

app.layout = html.Div(children=[
    html.Div(
        children=[
            html.H2(children="Mapa de Colombia", className='h2-title')
        ],
        className='study-browser-banner row'
    ),
    html.Div(
        children=[
                html.H6("Seleccione Municipio"),
                dcc.Dropdown(
                    id="study-dropdown",
                    multi=True,
                    value=('LA PRIMAVERA',),
                    options=[{'label': label.title(), 'value': label.title()} for label in df_correc['NOMBRE_MPI'].unique()]
                )
            ]
    ),
    html.Div(
        className='row app-body', 
        children=[
            html.Div(
                className='twelve columns card-left',
                children=[
                    html.Div(
                        dcc.Graph(id='map-plot', figure={ 
            'data': [go.Choroplethmapbox(
                geojson=geojson,
                locations=df_correc['MPIOS'],
                z=df_correc['HECTARES'],
                colorscale='earth',
                text=df_correc['NOMBRE_MPI'],
                colorbar_title="HECTAREAS"
            )],
            'layout': go.Layout(
                    mapbox_style="open-street-map",
                    mapbox_accesstoken=token,
                    mapbox_zoom=4,
                    margin={'t': 0, 'l': 0, 'r': 0, 'b': 0},
                    mapbox_center={"lat": 4.6109886, "lon": -74.072092}
                )
        }),
                    ),                     
                ])
            ]
        )]
)

if __name__ == "__main__":
    app.run_server(debug=True)