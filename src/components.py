from dataclasses import dataclass

import dash_bootstrap_components as dbc
from dash.dependencies import Input

POINTS_INPUTS = [Input(f"num-{index}", "n_clicks") for index in range(10)]


@dataclass
class Zvanje:
    value: int
    name: str


def make_zvanja_input() -> dbc.Row:
    return dbc.Row(
        [
            dbc.Col(dbc.Button("20", id="button-20", n_clicks=0, className="m-1")),
            dbc.Col(dbc.Button("50", id="button-50", n_clicks=0, className="m-1")),
            dbc.Col(dbc.Button("100", id="button-100", n_clicks=0, className="m-1")),
            dbc.Col(dbc.Button("150", id="button-150", n_clicks=0, className="m-1")),
            dbc.Col(dbc.Button("200", id="button-200", n_clicks=0, className="m-1")),
            dbc.Col(
                dbc.Button("štiglja", id="button-štiglja", n_clicks=0, className="m-1")
            ),
        ],
        justify="center",
        className="my-3",
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
