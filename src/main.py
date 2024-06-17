from enum import StrEnum, auto

import dash
import dash_bootstrap_components as dbc
from dash import dcc, html
from dash.dependencies import Input, Output, State

import components

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

MAX_SCORE = 162


class Team(StrEnum):
    TEAM_A = auto()
    TEAM_B = auto()


app.layout = dbc.Container(
    [
        components.score_containers(),
        components.sum_containers(),
        components.make_zvanja_input(),
        components.numpad(),
        components.round_select_buttons(),
        dcc.Store(id="selected_team", data=Team.TEAM_A),
        dcc.Store(id="score_team_a", data=0),
        dcc.Store(id="score_team_b", data=0),
        dcc.Store(id="extra_points_team_a", data=0),
        dcc.Store(id="extra_points_team_b", data=0),
    ],
    fluid=True,
    style={"max-width": "500px", "margin": "0 auto", "padding": "20px"},
)


@app.callback(
    [
        Output("container_score_team_a", "style", allow_duplicate=True),
        Output("container_score_team_b", "style", allow_duplicate=True),
    ],
    [Input("selected_team", "data")],
    [
        State("container_score_team_a", "style"),
        State("container_score_team_b", "style"),
    ],
    prevent_initial_call=True,
)
def update_button_style(selected_team: Team, green_style: dict, red_style: dict):
    highlighted_border_css = "4px solid #000000"
    normal_border = "4px"

    if selected_team == Team.TEAM_A:
        green_style["border"] = highlighted_border_css
        red_style["border"] = normal_border

    if selected_team == Team.TEAM_B:
        green_style["border"] = normal_border
        red_style["border"] = highlighted_border_css

    return green_style, red_style


@app.callback(
    Output("selected_team", "data"),
    [
        Input("container_score_team_a", "n_clicks"),
        Input("container_score_team_b", "n_clicks"),
    ],
    prevent_initial_call=True,
)
def update_selected_team(n_clicks_a: int, n_clicks_b: int):
    ctx = dash.callback_context
    clicked_button_id = ctx.triggered[0]["prop_id"].split(".")[0]

    if clicked_button_id == "container_score_team_a":
        return Team.TEAM_A

    if clicked_button_id == "container_score_team_b":
        return Team.TEAM_B


@app.callback(
    [
        Output("selected_team", "data", allow_duplicate=True),
        Output("score_team_a", "data", allow_duplicate=True),
        Output("score_team_b", "data", allow_duplicate=True),
        Output("extra_points_team_a", "data", allow_duplicate=True),
        Output("extra_points_team_b", "data", allow_duplicate=True),
        Output("container_score_team_a", "children", allow_duplicate=True),
        Output("container_score_team_b", "children", allow_duplicate=True),
    ],
    Input("button-odustani", "n_clicks"),
    prevent_initial_call=True,
)
def reset(n_clicks: int) -> tuple:
    return Team.TEAM_A, 0, 0, 0, 0, "0", "0"


@app.callback(
    Output("extra_points_team_a", "data", allow_duplicate=True),
    Output("extra_points_team_b", "data", allow_duplicate=True),
    [components.EXTRA_POINTS_INPUTS],
    [
        [State("extra_points_team_a", "data"), State("extra_points_team_b", "data")],
        State("selected_team", "data"),
    ],
    prevent_initial_call=True,
)
def update_extra_points(
    inputs: list[Input], current_extra_scores: list[State], selected_team: str
) -> tuple[int, int]:
    ctx = dash.callback_context
    app.logger.info(current_extra_scores)
    # if ctx.triggered[0]["value"] is None:
    #     return 0, 0

    extra_points_a, extra_points_b = current_extra_scores

    button_id = ctx.triggered[0]["prop_id"].split(".")[0]

    if button_id == "button-štiglja":
        return extra_points_a + 90, extra_points_b

    extra_points = int(button_id.split("-")[-1])

    if selected_team == Team.TEAM_A:
        new_score_a = extra_points_a + extra_points
        new_score_b = extra_points_b

    if selected_team == Team.TEAM_B:
        new_score_a = extra_points_a
        new_score_b = extra_points_b + extra_points

    return new_score_a, new_score_b


@app.callback(
    Output("score_team_a", "data", allow_duplicate=True),
    Output("score_team_b", "data", allow_duplicate=True),
    [components.POINTS_INPUTS],
    [[State("score_team_a", "data"), State("score_team_b", "data")]],
    prevent_initial_call=True,
)
def update_points(inputs: list[Input], scores: list[State]) -> None:
    ctx = dash.callback_context
    if ctx.triggered[0]["value"] is None:
        return 0, 0

    button_id = ctx.triggered[0]["prop_id"].split(".")[0]

    number = int(button_id.split("-")[-1])

    score_a, _ = scores

    if len(str(score_a)) == 3:
        return score_a, 162 - score_a

    new_score_a = min(162, int(str(score_a) + str(number)))
    new_score_b = max(0, 162 - new_score_a)

    return new_score_a, new_score_b


@app.callback(
    Output("extra_points_team_a", "data", allow_duplicate=True),
    Output("extra_points_team_b", "data", allow_duplicate=True),
    Input("button-reset-extra-points", "n_clicks"),
    prevent_initial_call=True,
)
def reset_extra_points(_) -> tuple[int, int]:
    return 0, 0


@app.callback(
    Output("score_team_a", "data", allow_duplicate=True),
    Output("score_team_b", "data", allow_duplicate=True),
    [Input("backspace", "n_clicks")],
    [[State("score_team_a", "data"), State("score_team_b", "data")]],
    prevent_initial_call=True,
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
    [
        Input("score_team_a", "data"),
        Input("score_team_b", "data"),
        Input("extra_points_team_a", "data"),
        Input("extra_points_team_b", "data"),
    ],
    prevent_initial_call=True,
    allow_duplicate=True,
)
def update_score_container(
    score_team_a: int, score_team_b: int, extra_points_a: int, extra_points_b: int
) -> tuple:
    return f"{score_team_a} + {extra_points_a}", f"{score_team_b} + {extra_points_b}"


if __name__ == "__main__":
    app.run(debug=True)
