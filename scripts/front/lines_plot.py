import plotly_express as px
import dash
import dash_html_components as html
import dash_core_components as dcc
import pandas as pd
import plotly.graph_objects as go
from dash.dependencies import Input, Output



df = pd.read_csv('tasa_desempleo.csv')

col_options = [dict(label=x, value=x) for x in df.columns]
dimensions = ["x (meses)", "y (tasa de desempleo)"]

app = dash.Dash(
    __name__, external_stylesheets=["https://codepen.io/chriddyp/pen/bWLwgP.css"]
)

app.layout = html.Div(
    [
        html.H1("Inverse survival plot"),
        html.Div(
            [
                html.P([d + ":", dcc.Dropdown(id=d, options=col_options)])
                for d in dimensions
            ],
            style={"width": "25%", "float": "left"},
        ),
        dcc.Graph(id="lineplot", style={"width": "75%", "display": "inline-block"}),
    ]
)


@app.callback(Output("lineplot", "figure"), [Input(d, "value") for d in dimensions])
def make_figure(x, y):
    fig = px.line(df, x=x, y=y, line_shape='spline', height=700, title='Mi análisis')
    fig.update_xaxes(title_text='Meses')
    fig.update_yaxes(title_text='Tasa de desempleo')
    fig.update_traces(hoverinfo='text+name', mode='lines+markers')
    return fig


app.run_server(debug=True)