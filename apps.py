import dash_mantine_components as dmc
from dash import Dash, html
from dash_iconify import DashIconify

app = Dash(__name__)

style_container = {
    "height": "100vh",
    # "border": f"1px solid {dmc.theme.DEFAULT_COLORS['indigo'][4]}",
    "marginTop": 20,
    "marginBottom": 20
}

style_grid1 = {
    "border": f"1px solid {dmc.theme.DEFAULT_COLORS['indigo'][4]}",
    "textAlign": "center",
}

app.layout = html.Div(
    children=[
        dmc.Container(
            [
                dmc.Header(
                    height=60,
                    children=[dmc.Group([
                        dmc.Text("Inventory Management Dashboard", weight=700),
                        dmc.Group(
                            [
                                dmc.ActionIcon(
                                    DashIconify(icon="iconamoon:mode-light-duotone", color="indigo", width=20)),
                                dmc.ActionIcon(DashIconify(icon="ph:eye-duotone", color="indigo", width=20)),
                                dmc.ActionIcon(DashIconify(icon="gridicons:user-circle", color="indigo", width=20)),
                            ],
                        ),
                    ], position="apart"),
                    ],
                    style={"backgroundColor": "#9c86e2"},
                    p="md",
                ),

                # pseudo row
                dmc.Grid([
                    dmc.Col([
                        dmc.Select(
                            placeholder="Select Period",
                            id="framework-select3",
                            data=[
                                {"value": "react", "label": "React"},
                                {"value": "angular", "label": "Angular"},
                                {"value": "svelte", "label": "Svelte"},
                                {"value": "vue", "label": "Vue"},
                            ],
                            style={"width": 150},
                        ),
                        dmc.Text(id="selected-value3"),
                    ], span="content"),
                    dmc.Col([
                        dmc.Select(
                            placeholder="Select State",
                            id="framework-select4",
                            data=[
                                {"value": "react", "label": "React"},
                                {"value": "angular", "label": "Angular"},
                                {"value": "svelte", "label": "Svelte"},
                                {"value": "vue", "label": "Vue"},
                            ],
                            style={"width": 150},
                        ),
                        dmc.Text(id="selected-value4"),
                    ], span="auto"),
                ], mt=2, gutter="xs",),

                # row1
                dmc.Grid(
                    children=[
                        dmc.Col(
                            dmc.Card(
                                children=[
                                    dmc.CardSection(
                                        dmc.Group(
                                            children=[
                                                dmc.Text("Inventory Trend", weight=500),
                                                dmc.Group(
                                                    children=[
                                                        dmc.Select(
                                                            placeholder="Select one",
                                                            id="framework-select",
                                                            data=[
                                                                {"value": "react", "label": "React"},
                                                                {"value": "angular", "label": "Angular"},
                                                                {"value": "svelte", "label": "Svelte"},
                                                                {"value": "vue", "label": "Vue"},
                                                            ],
                                                            style={"width": 180},
                                                        ),
                                                        dmc.Text(id="selected-value"),
                                                        dmc.ActionIcon(
                                                            DashIconify(icon="ph:upload"),
                                                            color="gray",
                                                            variant="transparent",
                                                        ),
                                                    ],
                                                ),
                                            ],
                                            position="apart",
                                        ),
                                        withBorder=True,
                                        inheritPadding=True,
                                        py="xs",
                                    ),
                                    dmc.Text(
                                        children=[
                                            dmc.Text(
                                                "200+ images uploaded",
                                                color="blue",
                                                style={"display": "inline"},
                                            ),
                                            " since last visit, review them to select which one should be added to your gallery",
                                        ],
                                        mt="sm",
                                        color="dimmed",
                                        size="sm",
                                    ),
                                ],
                                withBorder=True,
                                shadow="sm",
                                radius="xs",
                                mt="xs",
                            ), span=5),
                        dmc.Col(
                            dmc.Card([
                                dmc.CardSection([
                                    dmc.Stack([
                                        dmc.Card(
                                            children=[
                                                dmc.Text(
                                                    "With Fjord Tours you can explore more of the magical fjord landscapes with tours and activities on and around the fjords of Norway",
                                                    size="sm",
                                                    color="dimmed",
                                                ),
                                            ],
                                            withBorder=True,
                                            shadow="sm",
                                            radius="xs",
                                        ),
                                        dmc.Card(
                                            children=[
                                                dmc.Text(
                                                    "With Fjord Tours you can explore more of the magical fjord landscapes with tours and activities on and around the fjords of Norway",
                                                    size="sm",
                                                    color="dimmed",
                                                ),
                                            ],
                                            withBorder=True,
                                            shadow="sm",
                                            radius="xs",
                                        )
                                    ], align="center",
                                        spacing="xs", ),
                                ],
                                    # style=style_grid1,
                                ),
                            ]),
                            span=2,
                            mt="xs",
                        ),
                        dmc.Col(
                            dmc.Card(
                                children=[
                                    dmc.CardSection(
                                        dmc.Group(
                                            children=[
                                                dmc.Text("Total Valuation", weight=500),
                                                dmc.Group(
                                                    children=[
                                                        dmc.ActionIcon(
                                                            DashIconify(icon="ph:upload"),
                                                            color="gray",
                                                            variant="transparent",
                                                        ),
                                                    ],
                                                    position="apart",
                                                ),
                                            ],
                                            position="apart",
                                        ),
                                        withBorder=True,
                                        inheritPadding=True,
                                        py="xs",
                                    ),
                                    dmc.Text(
                                        children=[
                                            dmc.Text(
                                                "200+ images uploaded",
                                                color="blue",
                                                style={"display": "inline"},
                                            ),
                                            " since last visit, review them to select which one should be added to your gallery",
                                        ],
                                        mt="sm",
                                        color="dimmed",
                                        size="sm",
                                    ),
                                ],
                                withBorder=True,
                                shadow="sm",
                                radius="xs",
                                mt="xs",
                            ), span=5),
                    ],
                    justify="center",
                    align="top",
                    gutter="xs",
                ),
                # row2
                dmc.Grid([
                    dmc.Col(
                        dmc.Card(
                            children=[
                                dmc.CardSection(
                                    dmc.Group(
                                        children=[
                                            dmc.Text("Inventory Management", weight=500),
                                            dmc.Group(
                                                children=[
                                                    dmc.ActionIcon(
                                                        DashIconify(icon="ph:upload"),
                                                        color="gray",
                                                        variant="transparent",
                                                    ),
                                                ],
                                                position="apart",
                                            ),
                                        ],
                                        position="apart",
                                    ),
                                    withBorder=True,
                                    inheritPadding=True,
                                    py="xs",
                                ),
                                dmc.Text(
                                    children=[
                                        dmc.Text(
                                            "200+ images uploaded",
                                            color="blue",
                                            style={"display": "inline"},
                                        ),
                                        " since last visit, review them to select which one should be added to your gallery",
                                    ],
                                    mt="sm",
                                    color="dimmed",
                                    size="sm",
                                ),
                            ],
                            withBorder=True,
                            shadow="sm",
                            radius="xs",
                            mt="xs",
                        ), span=4),
                    dmc.Col(
                        dmc.Card(
                            children=[
                                dmc.CardSection(
                                    dmc.Group(
                                        children=[
                                            dmc.Text("Total Stock Overview", weight=500),
                                            dmc.Group(
                                                children=[
                                                    dmc.ActionIcon(
                                                        DashIconify(icon="ph:upload"),
                                                        color="gray",
                                                        variant="transparent",
                                                    ),
                                                ],
                                                position="apart",
                                            ),
                                        ],
                                        position="apart",
                                    ),
                                    withBorder=True,
                                    inheritPadding=True,
                                    py="xs",
                                ),
                                dmc.Text(
                                    children=[
                                        dmc.Text(
                                            "200+ images uploaded",
                                            color="blue",
                                            style={"display": "inline"},
                                        ),
                                        " since last visit, review them to select which one should be added to your gallery",
                                    ],
                                    mt="sm",
                                    color="dimmed",
                                    size="sm",
                                ),
                            ],
                            withBorder=True,
                            shadow="sm",
                            radius="xs",
                            mt="xs",
                        ), span=8),
                ],
                    justify="center",
                    align="top",
                    gutter="xs", )
            ],
            style=style_container,
            fluid=True,
        ),
    ]
)

if __name__ == "__main__":
    app.run_server()
