from dataclasses import dataclass

import dash_bootstrap_components as dbc
from dash.dependencies import Input

POINTS_INPUTS = [Input(f"num-{index}", "n_clicks") for index in range(10)]


@dataclass
class Zvanje:
    value: int
    name: str


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
