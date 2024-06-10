import pandas as pd
import plotly.express as px
import dash_bootstrap_components as dbc
from dash import dcc, html, Dash, dash_table

# dcc --- Dash Core Components
# html --- Dash Html Components
# Date,MSFT,FB,AAPL

def dash_layout(data:pd.DataFrame):
    fig = px.line(data, x="Date", y=["MSFT", "FB", "AAPL"], title="Microsoft Stocks")
    body = html.Div([
        html.H1("Datos Stocks", style={"textAlign":"center", "color":"blue"}),
        html.P("Objetivo DashBoard: Mostrar los Stocks semanales de Microsoft, Apple, Facebook."),
        html.Hr(),
        dash_table.DataTable(data=data.to_dict("records"), page_size=10),
        dcc.Graph(figure=fig)
    ])
    return body


if __name__ == "__main__":
    data = pd.read_csv("datasets/weekly_stocks.csv")
    app = Dash(__name__)
    app.layout= dash_layout(data)
    app.run(debug=True)


    fig = px.line(data, x="Date", y=["MSFT", "FB", "AAPL"], title="Microsoft Stocks")
    fig_area = px.area(data, x="Date", y=["MSFT", "FB", "AAPL"])
    fig_area.update_layout(xaxis_title="Date", yaxis_title="Stocks", title="Stocks Semanales")
    fig_scatter = px.scatter(data, x="Date", y="MSFT",
                             color="MSFT", size="MSFT")

    iris = px.data.iris()
    fig_iris = px.scatter(iris, x="species", y="petal_width", size="petal_length", color="species")
    print(iris.sample(10))

    #fig_iris.show()
    #fig.show()
    #fig_area.show()
    #fig_scatter.show()