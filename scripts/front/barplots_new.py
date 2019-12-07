import pandas as pd
import requests
import flask
import json
from pandas.io.json import json_normalize
import plotly_express as px
import dash
import dash_html_components as html
import dash_core_components as dcc
import plotly.graph_objects as go
from dash.dependencies import Input, Output

def get_rows(str_query=None):
    response = requests.post("http://ec2-3-133-150-215.us-east-2.compute.amazonaws.com:8020/raw_query", json={"raw_query": str_query})
    return response.json()


sexo = 'Mujer'
mes = 12
mes = str(mes)

# Ingresos por educación

ing_educ_query = "select \"Nivel educativo\", avg(\"Ingresos\") as \"Ingreso promedio\" from view_ocupados_desocupados"
filters = "where mes =" + mes + "and \"Sexo\" = '" + sexo + "' and \"Ocupado\" is True "
groupby = "group by \"Nivel educativo\""
orderby = "order by \"Ingreso promedio\" DESC;"
ing_educ_query = ing_educ_query + ' ' + filters + ' ' + groupby + ' ' + orderby

df_ing_educ = get_rows(ing_educ_query)
df_ing_educ = pd.DataFrame.from_dict(df_ing_educ['data']['table'])
df_ing_educ['Ingreso promedio'] = round(df_ing_educ['Ingreso promedio'])
df_ing_educ.dropna(inplace=True)
print(df_ing_educ)


# Ingresos por ocupaciones

ing_ocu_query = "select \"Ocupación\", avg(\"Ingresos\") as \"Ingreso promedio\" from view_ocupados_desocupados"
filters = "where mes = " + mes + "and \"Ocupación\" <> 'ND' and \"Sexo\" = '" + sexo + "' and \"Ocupado\" is True "
groupby = "group by \"Ocupación\""
orderby = "order by \"Ingreso promedio\" DESC;"
ing_ocu_query = ing_ocu_query + ' ' + filters + ' ' + groupby + ' ' + orderby


df_ing_ocu = get_rows(ing_ocu_query)
df_ing_ocu = pd.DataFrame.from_dict(df_ing_ocu['data']['table'])
df_ing_ocu['Ingreso promedio'] = round(df_ing_ocu['Ingreso promedio'])
df_ing_ocu.dropna(inplace=True)
print(df_ing_ocu)



## Desempleo por ocupaciones

unemp_ocup_query = "select \"Ocupación\", round(100-100*(sum(\"Ocupado\"::INTEGER::FLOAT) / count(*)::FLOAT)::NUMERIC, 2) as \"Tasa de desempleo\" from view_ocupados_desocupados"
filters = "where mes = " + mes + "and \"Ocupación\" <> 'ND' and \"Sexo\" = '" + sexo + "'" 
groupby = "group by \"Ocupación\""
orderby = "order by \"Tasa de desempleo\" desc;"
unemp_ocup_query = unemp_ocup_query + ' ' + filters + ' ' + groupby + ' ' + orderby

df_unemp_ocup = get_rows(unemp_ocup_query)
df_unemp_ocup = pd.DataFrame.from_dict(df_unemp_ocup['data']['table'])
df_unemp_ocup.dropna(inplace=True)
print(df_unemp_ocup)



app = dash.Dash(
    __name__, external_stylesheets=["https://codepen.io/chriddyp/pen/bWLwgP.css"]
)

app.layout = html.Div(
    [
        html.H1("Ingresos y nivel educativo"),
        dcc.Graph(id="ing_educ", style={"width": "75%", "display": "inline-block"},
        figure = px.bar(df_ing_educ, x='Nivel educativo', y='Ingreso promedio')),

        html.H1("Ingresos y ocupación"),
        dcc.Graph(id="ing_ocup", style={"width": "75%", "display": "inline-block"},
        figure = px.bar(df_ing_ocu, x='Ocupación', y='Ingreso promedio')),

        html.H1("Tasa de desempleo por ocupación"),
        dcc.Graph(id="unemp_ocup", style={"width": "75%", "display": "inline-block"},
        figure = px.bar(df_unemp_ocup, x='Ocupación', y='Tasa de desempleo')),

    ]
)


# @app.callback(Output("dot", "figure"), [Input(d, "value") for d in dimensions])
# def make_figure(x, y):
#     fig = px.scatter(df, x=x, y=y, height=700, title='Mi análisis')
#     #fig.update_xaxes(title_text='Meses')
#     #fig.update_yaxes(title_text='Tasa de desempleo')
#     #fig.update_traces(hoverinfo='text+name', mode='lines+markers')
#     return fig


app.run_server(debug=True)