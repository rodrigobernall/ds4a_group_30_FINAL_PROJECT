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
                    value=('SANTAFE DE BOGOTA D.C.',),
                    options=[{'label': label, 'value': label} for label in df_correc['NOMBRE_MPI'].unique()]
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
                            'data': [go.Choroplethmapbox()],
                            'layout': go.Layout(
                                    mapbox_style="dark",
                                    mapbox_accesstoken=token,
                                    mapbox_zoom=5,
                                    margin={'t': 0, 'l': 0, 'r': 0, 'b': 0},
                                    mapbox_center={"lat": 4.6109886, "lon": -74.072092}
                                )
        }),
                    ),                     
                ])
            ]
        )]
)

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


if __name__ == "__main__":
    app.run_server(debug=True)