import dash_bootstrap_components as dbc
from dash import html
from dash.dependencies import Input

EXTRA_POINTS_INPUTS = [
    Input(f"button-{num}", "n_clicks") for num in [20, 50, 100, 150, 200]
] + [Input("button-štiglja", "n_clicks")]
POINTS_INPUTS = [Input(f"num-{index}", "n_clicks") for index in range(10)]


def make_zvanja_input() -> dbc.Row:
    def _button_cell(children: str, id: str) -> dbc.Col:
        return dbc.Col(
            dbc.Button(
                children,
                id=id,
                n_clicks=0,
                style={
                    "width": "100%",
                    "height": "100%",
                    "border": "1px solid black",
                    "backgroundColor": "#f8f9fa",
                    "color": "black",
                },
            )
        )

    return dbc.Row(
        [
            dbc.Row(
                [
                    _button_cell("20", "button-20"),
                    _button_cell("50", "button-50"),
                    _button_cell("100", "button-100"),
                ],
                justify="center",
            ),
            dbc.Row(
                [
                    _button_cell("150", "button-150"),
                    _button_cell("200", "button-200"),
                    _button_cell("Štiglja", "button-štiglja"),
                ],
                justify="center",
            ),
        ],
        justify="center",
        style={
            "backgroundColor": "#e8eae9",
            "padding": "10px",
        },
    )


def numpad() -> dbc.Row:
    def _numpad_button(children: str, id: str) -> dbc.Button:
        return dbc.Button(
            children,
            id=id,
            n_clicks=0,
            className="m-1",
            style={
                "width": "100%",
                "height": "100%",
                "padding": "10px",
                "border": "1px solid black",
                "backgroundColor": "#f8f9fa",  # Off-white color
                "color": "black",  # Text color
            },
        )

    rows = []
    for row_number in range(3):
        cols = []
        for col_number in range(1, 4):
            input_number = 3 * row_number + col_number
            col = dbc.Col(
                _numpad_button(children=str(input_number), id=f"num-{input_number}"),
                width=4,
            )
            cols.append(col)

        rows.append(dbc.Row(cols))

    zero_row = dbc.Row(
        [
            dbc.Col(_numpad_button(children="", id="empty-button"), width=4),
            dbc.Col(_numpad_button(children="0", id="num-0"), width=4),
            dbc.Col(_numpad_button(children="<", id="backspace"), width=4),
        ]
    )

    rows.append(zero_row)

    return dbc.Row(
        rows,
        justify="center",
        className="my-3",
    )


def round_select_buttons() -> dbc.Row:
    return dbc.Row(
        [
            dbc.Col(
                dbc.Button(
                    "Odustani",
                    id="button-odustani",
                    href="/",
                    n_clicks=0,
                    style={
                        "width": "100%",
                        "height": "100%",
                        "padding": "10px",
                        "border": "1px solid black",
                        "backgroundColor": "#f8f9fa",  # Off-white color
                        "color": "black",  # Text color
                    },
                ),
                width=3,
            ),
            dbc.Col(
                dbc.Button(
                    "Spremi",
                    id="button-spremi",
                    n_clicks=0,
                    style={
                        "width": "100%",
                        "height": "100%",
                        "padding": "10px",
                        "border": "1px solid black",
                        "backgroundColor": "#A0A7A4",  # Off-white color
                        "color": "white",  # Text color
                    },
                ),
                width=3,
            ),
            dbc.Col(
                dbc.Button(
                    "Poništi zvanja",
                    id="button-reset-extra-points",
                    n_clicks=0,
                    style={
                        "width": "100%",
                        "height": "100%",
                        "padding": "10px",
                        "border": "1px solid black",
                        "backgroundColor": "#EF9A93",  # Off-white color
                        "color": "black",  # Text color
                    },
                ),
                width=3,
            ),
        ],
        justify="between",
    )


def sum_containers() -> dbc.Row:
    return dbc.Row(
        [
            dbc.Col(html.Div(id="sum1", children="Σ 0", className="text-center my-2")),
            dbc.Col(html.Div(id="sum2", children="Σ 0", className="text-center my-2")),
        ],
        justify="center",
    )


def score_containers() -> dbc.Row:
    return dbc.Row(
        [
            dbc.Col(
                dbc.Button(
                    "0",
                    id="container_score_team_a",
                    style={
                        "width": "100%",
                        "height": "100%",
                        "font-size": "20px",
                        "border": "4px solid #000000",
                        "backgroundColor": "#2F974B",
                        "color": "black",
                        "display": "flex",
                        "justify-content": "center",
                        "align-items": "center",
                        "margin": "auto",
                    },
                ),
                width=6,
                style={"display": "flex", "justify-content": "center"},
            ),
            dbc.Col(
                dbc.Button(
                    "0",
                    id="container_score_team_b",
                    style={
                        "width": "100%",
                        "height": "100%",
                        "font-size": "20px",
                        "border": "4px",
                        "backgroundColor": "#F03A3A",
                        "color": "black",
                        "display": "flex",
                        "justify-content": "center",
                        "align-items": "center",
                        "margin": "auto",
                    },
                ),
                width=6,
                style={"display": "flex", "justify-content": "center"},
            ),
        ],
        justify="center",
    )
