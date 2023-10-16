from dash import Dash, dcc, html
import dash_bootstrap_components as dbc

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP, dbc.icons.FONT_AWESOME])

row1 = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink(html.I(className="fas fa-cog"))),
        dbc.NavItem(dbc.NavLink(html.I(className="fas fa-eye"))),
        dbc.NavItem(dbc.NavLink(html.I(className="fas fa-user"))),
    ],
    brand="Inventory Management Dashboard",
    brand_href="#",
    color="primary",
    dark=True,
)

row2 = dbc.CardGroup(
    [
        #left col
        dbc.Card([
            dbc.CardHeader(["Inventory Trend",
                                dbc.Stack(
                                            [
                                                dbc.DropdownMenu(
                                                        label="dropdown1",
                                                            children=[
                                                                dbc.DropdownMenuItem("Item 1"),
                                                                dbc.DropdownMenuItem("Item 2"),
                                                                dbc.DropdownMenuItem("Item 3"),
                                                            ], className="ms-auto", size="sm",
                                                        ),
                                                dbc.DropdownMenu(
                                                        label="dropdown2",
                                                            children=[
                                                                dbc.DropdownMenuItem("Item 1"),
                                                                dbc.DropdownMenuItem("Item 2"),
                                                                dbc.DropdownMenuItem("Item 3"),
                                                            ], className="ms-auto", size="sm",
                                                        ),
                                                html.I(className="fas fa-upload "),
                                            ],
                                            direction="horizontal",
                                            gap=3,
                                ),
                           ]),
            dbc.CardBody(
                [
                    html.H5("Card 1", className="card-title"),
                    html.P(
                        "This card has some text content, which is a little "
                        "bit longer than the second card.",
                        className="card-text",
                    ),
                ]
            )
        ]),

        #middle col
        dbc.Card([
            dbc.CardBody(
                [
                    dbc.Stack(
                        [
                                    dbc.Stack(
                                                [
                                                            dbc.Card(
                                                                dbc.CardBody(
                                                                    [
                                                                        html.H5("Card title", className="card-title"),
                                                                        html.P("This card has some text content, but not much else"),
                                                                    ]
                                                                )
                                                            ),
                                                            dbc.Card(
                                                                dbc.CardBody(
                                                                    [
                                                                        html.H5("Card title", className="card-title"),
                                                                        html.P("This card has some text content, but not much else"),
                                                                    ]
                                                                )
                                                            ),
                                                ],
                                                gap=3,
                                    ),

                                    dbc.Stack(
                                                [
                                                            dbc.Card(
                                                                dbc.CardBody(
                                                                    [
                                                                        html.H5("Card title", className="card-title"),
                                                                        html.P("This card has some text content, but not much else"),
                                                                    ]
                                                                )
                                                            ),
                                                            dbc.Card(
                                                                dbc.CardBody(
                                                                    [
                                                                        html.H5("Card title", className="card-title"),
                                                                        html.P("This card has some text content, but not much else"),
                                                                    ]
                                                                )
                                                            ),
                                                ],
                                                gap=3,
                                    ),
                        ],
                        direction="horizontal",
                        gap=3,
                    ),
                ]
            )
        ]),

        #right Col
        dbc.Card([
            dbc.CardHeader(["Log Activity"]),
            dbc.CardBody(
                [
                    html.H5("Card 3", className="card-title"),
                    html.P(
                        "This card has some text content, which is longer "
                        "than both of the other two cards, in order to "
                        "demonstrate the equal height property of cards in a "
                        "card group.",
                        className="card-text",
                    ),
                ]
            )
        ]),
    ],
)


app.layout = dbc.Container([
                row1,
                row2,
                ])


if __name__ == '__main__':
    app.run_server(debug=True)
