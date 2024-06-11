import dash
import dash_bootstrap_components as dbc
from dash import html, dcc
from dash.dependencies import Input, Output, State

import components

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

MAX_SCORE = 162

app.layout = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    html.Div(
                        id="score1",
                        children="0",
                        className="p-3 mb-2 bg-success text-white text-center",
                    )
                ),
                dbc.Col(
                    html.Div(
                        id="score2",
                        children="0",
                        className="p-3 mb-2 bg-danger text-white text-center",
                    )
                ),
            ],
            justify="center",
        ),
        dbc.Row(
            [
                dbc.Col(
                    html.Div(id="sum1", children="Σ 0", className="text-center my-2")
                ),
                dbc.Col(
                    html.Div(id="sum2", children="Σ 0", className="text-center my-2")
                ),
            ],
            justify="center",
        ),
        components.make_zvanja_input(),
        components.numpad(),
        dbc.Row(
            [
                dbc.Col(
                    dbc.Button(
                        "Odustani", id="button-odustani", n_clicks=0, className="m-1"
                    ),
                    width=6,
                ),
                dbc.Col(
                    dbc.Button(
                        "Spremi", id="button-spremi", n_clicks=0, className="m-1"
                    ),
                    width=6,
                ),
            ],
            justify="between",
            className="my-3",
        ),
    ],
    fluid=True,
    style={"max-width": "500px", "margin": "0 auto", "padding": "20px"},
)


@app.callback(
    Output("score1", "children"),
    Output("score2", "children"),
    Output("sum1", "children"),
    Output("sum2", "children"),
    [
        Input("button-20", "n_clicks"),
        Input("button-50", "n_clicks"),
        Input("button-100", "n_clicks"),
        Input("button-150", "n_clicks"),
        Input("button-200", "n_clicks"),
    ],
    [State("score1", "children"), State("score2", "children")],
)
def update_scores(b20, b50, b100, b150, b200, score1, score2):
    ctx = dash.callback_context
    if not ctx.triggered:
        return score1, score2, "Σ 0", "Σ 0"
    else:
        button_id = ctx.triggered[0]["prop_id"].split(".")[0]

        if button_id == "button-20":
            score1 = int(score1) + 20
        elif button_id == "button-50":
            score1 = int(score1) + 50
        elif button_id == "button-100":
            score1 = int(score1) + 100
        elif button_id == "button-150":
            score1 = int(score1) + 150
        elif button_id == "button-200":
            score1 = int(score1) + 200

    sum1 = f"Σ {score1}"
    sum2 = f"Σ {score2}"
    return score1, score2, sum1, sum2


@app.callback(
    outputs=[
        Output("score1", "children"),
        Output("score2", "children"),
        Output("sum1", "children"),
        Output("sum2", "children"),
    ],
    inputs=components.POINTS_INPUTS,
    states=[State("score1", "children"), State("score2", "children")],
)
def update_points(inputs: list[Input], states: list[State]) -> None:
    ctx = dash.callback_context
    if not ctx.triggered:
        return 0, 0

    button_id = ctx.triggered[0]["prop_id"].split(".")[0]

    if button_id == "button-20":
        score1 = int(score1) + 20
    elif button_id == "button-50":
        score1 = int(score1) + 50
    elif button_id == "button-100":
        score1 = int(score1) + 100
    elif button_id == "button-150":
        score1 = int(score1) + 150
    elif button_id == "button-200":
        score1 = int(score1) + 200

    return score1, score2


# @app.callback(
#     None,
#     [Input("button-spremi", "n_clicks")],
#     [State("score1", "children"), State("score2", "children")],
# )
# def save_round():
#     pass


if __name__ == "__main__":
    app.run(debug=True)
