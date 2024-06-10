import pandas as pd
import plotly.express as px
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
#Date,MSFT,FB,AAPL

def filtros():
    tarejeta_filtro = dbc.Card(
        dbc.CardBody([
            html.Div([
                dbc.Label("Compania"),
                dcc.Dropdown(options=["All","Apple","Facebook", "Microsoft"])
                    ]),
                html.Div([
                    dbc.Label("Year:"),
                    dbc.Input()
                ])
        ])
    )
    return tarejeta_filtro

def dashboard(data:pd.DataFrame):
    fig_line = px.line(data, x="Date", y=["MSFT", "FB", "AAPL"], title="Microsoft stocks")

    body = html.Div([

        html.H2("Stocks Semanales", style={"textAlign":"center","color":"red"}),
        html.P("Objetivo:Mostrar los stocks semanales de microsoft, apple y facebook"),
        html.Hr(),
        dbc.Row([
            dbc.Col(filtros()),
            dbc.Col([
            ]),
        ]),
        dcc.Graph(figure=fig_line)
    ])
    return body

if __name__ == "__main__":
    data = pd.read_csv("Datasets/weekly_stocks.csv")

    fig_line = px.line(data,x="Date", y=["MSFT","FB","AAPL"], title="Microsoft stocks")
    fig_area = px.area(y=["MSFT","FB","AAPL"], title="Microsoft stocks")
    fig_scatter = px.scatter(data, x="Date",y="MSFT")
    fig_scatter.update_layout(xaxis_title= "dia",yaxis_title="stocks semanales")
    fig_scatter.show()
    #print(data)

    app = Dash(__name__, external_stylesheets=[dbc.themes.FLATLY])
    app.layout = dashboard(data)
    app.run(debug=True)