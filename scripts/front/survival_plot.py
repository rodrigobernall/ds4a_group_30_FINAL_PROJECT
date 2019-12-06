import plotly_express as px
import dash
import dash_html_components as html
import dash_core_components as dcc
import pandas as pd
import plotly.graph_objects as go
from dash.dependencies import Input, Output



df = pd.read_csv('survival_nivel_educ.csv')
df['fact'] = pd.Categorical(df['fact'].astype(int))
df.columns = ['index', 'Meses', 'Porcentaje de personas', 'grouper'] 
df.drop(columns=['index'], inplace=True)
df['Porcentaje de personas'] = (df['Porcentaje de personas'])*100
 
col_options = [dict(label=x, value=x) for x in df.columns]
dimensions = ["x (meses)", "y (porcentaje)", "grouper"]

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
        dcc.Graph(id="graph", style={"width": "75%", "display": "inline-block"}),
    ]
)


@app.callback(Output("graph", "figure"), [Input(d, "value") for d in dimensions])
def make_figure(x, y, color):
    fig = px.line(df, x=x, y=y, color=color, line_shape='hv', height=700, title='Mi análisis')
    fig.update_xaxes(title_text='Seguirá desempleada después de estos meses')
    fig.update_yaxes(title_text='Este porcentaje de personas')#, range=[0,60])
    return fig


app.run_server(debug=True)