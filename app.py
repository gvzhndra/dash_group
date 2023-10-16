from dash import Dash, dcc, html
import dash_bootstrap_components as dbc

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP, dbc.icons.FONT_AWESOME])

app.layout = dbc.Container([
    #1st row
    dbc.Row([
        dbc.Col(html.H2("Inventory Management Dashboard"),
                width=8, className="bg-primary"),
        dbc.Col([
            html.I(className="fas fa-eye align-middle"),
            html.I(className="fas fa-user align-middle"),
            html.I(className="fas fa-check-circle align-middle"),
        ], width=4, className="bg-light"),
    ]),

    #2nd row
    dbc.Row([
        dbc.Col(dbc.Card(
            [
                dbc.CardHeader("This is the header"),
                dbc.CardBody([
                    html.H4("Card title", className="card-title"),
                    html.P("This is some card text", className="card-text"),
                ]),
            ],
        ), width=5, className="bg-info"),
        dbc.Col([
            dbc.Row([
                dbc.Col(dbc.Card(dbc.CardBody("Card 1")), width=6),
                dbc.Col(dbc.Card(dbc.CardBody("Card 2")), width=6),
            ]),
            dbc.Row([
                dbc.Col(dbc.Card(dbc.CardBody("Card 3")), width=6),
                dbc.Col(dbc.Card(dbc.CardBody("Card 4")), width=6),
            ]),
        ], width=3, className="bg-success"),
        dbc.Col(dbc.Card(
            [
                dbc.CardHeader("This is the header"),
                dbc.CardBody([
                    html.H4("Card title", className="card-title"),
                    html.P("This is some card text", className="card-text"),
                ]),
            ],
        ), width=4, className="bg-info"),
    ]),

    #3rd row
    dbc.Row([
            dbc.Col(dbc.Card(
                [
                    dbc.CardHeader("This is the header"),
                    dbc.CardBody([
                        html.H4("Card title", className="card-title"),
                        html.P("This is some card text", className="card-text"),
                    ]),
                ],
            ), width=8, className="bg-secondary"),
            dbc.Col(dbc.Card(
                [
                    dbc.CardHeader("This is the header"),
                    dbc.CardBody([
                        html.H4("Card title", className="card-title"),
                        html.P("This is some card text", className="card-text"),
                    ]),
                ],
            ), width=4, className="bg-primary"),
        ]),
   ])

if __name__ == '__main__':
    app.run_server(debug=True)
