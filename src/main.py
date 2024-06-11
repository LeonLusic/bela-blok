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
                        id="container_score_team_a",
                        children="0",
                        className="p-3 mb-2 bg-success text-white text-center",
                    )
                ),
                dbc.Col(
                    html.Div(
                        id="container_score_team_b",
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
        dcc.Store(id="selected_team", data="team_a"),
        dcc.Store(id="score_team_a", data=0),
        dcc.Store(id="score_team_b", data=0),
    ],
    fluid=True,
    style={"max-width": "500px", "margin": "0 auto", "padding": "20px"},
)



@app.callback(
    Output("score_team_a", "data", allow_duplicate=True),
    Output("score_team_b", "data", allow_duplicate=True),
    [components.POINTS_INPUTS],
    [[State("score_team_a", "data"), State("score_team_b", "data")]],
    prevent_initial_call=True,
)
def update_points(inputs: list[Input], states: list[State]) -> None:
    ctx = dash.callback_context
    if ctx.triggered[0]["value"] is None:
        return 0, 0

    button_id = ctx.triggered[0]["prop_id"].split(".")[0]

    number = int(button_id.split("-")[-1])

    score_a, _ = states

    if len(str(score_a)) == 3:
        return score_a, 162 - score_a
    
    new_score_a = min(162, int(str(score_a) + str(number)))
    new_score_b = max(0, 162 - new_score_a)

    return new_score_a, new_score_b


@app.callback(
    Output("score_team_a", "data", allow_duplicate=True),
    Output("score_team_b", "data", allow_duplicate=True),
    [Input("backspace", "n_clicks")],
    [[State("score_team_a", "data"), State("score_team_b", "data")]],
    prevent_initial_call=True
)
def backspace_points(inputs: list[Input], states: list[State]) -> None:
    ctx = dash.callback_context
    if ctx.triggered[0]["value"] is None:
        return states

    score_a, _ = states

    if score_a < 10:
        return 0, 162
    
    new_score_a = max(0, int(str(score_a)[:-1]))
    new_score_b = min(162, 162 - new_score_a)

    return new_score_a, new_score_b

@app.callback(
    Output("container_score_team_a", "children", allow_duplicate=True),
    Output("container_score_team_b", "children", allow_duplicate=True),
    [Input("score_team_a", "data"), Input("score_team_b", "data")],
    prevent_initial_call=True,
    allow_duplicate=True
)
def update_score_container(score_team_a: int, score_team_b: int) -> tuple:
    return score_team_a, score_team_b


if __name__ == "__main__":
    app.run(debug=True)
