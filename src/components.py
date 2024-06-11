import dash_bootstrap_components as dbc

from dataclasses import dataclass

from dash.dependencies import Input, Output, State


POINTS_INPUTS = [Input(f"num-{index}", "value") for index in range(10)]


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
    rows = []
    for row_number in range(3):
        cols = []
        for col_number in range(1, 4):
            input_number = 3 * row_number + col_number
            col = dbc.Col(
                dbc.Button(
                    str(input_number),
                    id=f"num-{input_number}",
                    n_clicks=0,
                    className="m-1",
                )
            )
            cols.append(col)

        rows.append(dbc.Row(cols))

    zero_row = dbc.Row(
        [
            dbc.Col(dbc.Button("", id="empty-button", n_clicks=0, class_name="m-1")),
            dbc.Col(dbc.Button("0", id="num-0", n_clicks=0, class_name="m-1")),
            dbc.Col(dbc.Button("<", id="backspace", n_clicks=0, class_name="m-1")),
        ]
    )

    rows.append(zero_row)

    return dbc.Row(
        rows,
        justify="center",
        className="my-3",
    )
