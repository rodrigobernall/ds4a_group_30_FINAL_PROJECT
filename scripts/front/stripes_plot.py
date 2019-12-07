import plotly_express as px
import dash
import dash_html_components as html
import dash_core_components as dcc
import pandas as pd
import plotly.graph_objects as go
from dash.dependencies import Input, Output



df = pd.read_csv('survival_nivel_educ.csv')
df['fact'] = pd.Categorical(df['fact'].astype(int))
df.columns = ['index', 'Meses', 'Porcentaje de personas', 'Categoría'] 
df.drop(columns=['index', 'Porcentaje de personas'], inplace=True)
#df['Porcentaje de personas'] = (df['Porcentaje de personas'])*100

col_options = [dict(label=x, value=x) for x in df.columns]
dimensions = ["x", "y"]

app = dash.Dash(
    __name__, external_stylesheets=["https://codepen.io/chriddyp/pen/bWLwgP.css"]
)

app.layout = html.Div(
    [
        html.H1("Survival analysis"),
        html.Div(
            [
                html.P([d + ":", dcc.Dropdown(id=d, options=col_options)])
                for d in dimensions
            ],
            style={"width": "25%", "float": "left"},
        ),
        dcc.Graph(id="stripplot", style={"width": "75%", "display": "inline-block"}),
    ]
)


@app.callback(Output("stripplot", "figure"), [Input(d, "value") for d in dimensions])
def make_figure(x, y):
    fig = px.strip(df, x=x, y=y, height=700, title='Mi análisis')
    fig.update_xaxes(title_text='Meses')
    fig.update_yaxes(title_text='Tasa de desempleo')
    fig.update_traces(hoverinfo='text+name', mode='lines+markers')
    return fig


app.run_server(debug=True)

#gshfkwufywt735281!