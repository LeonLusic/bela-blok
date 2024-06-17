from dataclasses import dataclass
from enum import StrEnum, auto

import dash
import dash_bootstrap_components as dbc
from dash import dcc, html
from dash.dependencies import Input, Output, State

import components

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP], use_pages=True)

MAX_SCORE = 162


class Team(StrEnum):
    TEAM_A = auto()
    TEAM_B = auto()


@dataclass
class Round:
    team_a: str
    team_b: str
    scores: tuple[int, int]
    extra_scores: tuple[int, int]


@dataclass
class Game:
    team_a: str
    team_b: str
    rounds: list[Round]
    winner: str
    winner_team_index: int


app.layout = dbc.Container(
    [
        dash.page_container,
        dcc.Location(id="url", refresh=False),
        dcc.Store(id="rounds", data=[]),
        dcc.Store(id="games", data=[]),
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
    [Output("mi-game-wins", "children"), Output("vi-game-wins", "children")],
    Input("games", "data"),
)
def update_round_wins(games: list[Game]) -> tuple[int, int]:
    team_a_wins = sum(1 for game in games if game.winner_team_index == 0)
    team_b_wins = sum(1 for game in games if game.winner_team_index == 1)

    return team_a_wins, team_b_wins


@app.callback(
    [Output("mi-ukupno", "children"), Output("vi-ukupno", "children")],
    Input("rounds", "data"),
)
def update_ukupno(rounds: list[Round]) -> tuple[int, int]:
    if rounds == []:
        return 0, 0

    team_a_total = sum(
        round["scores"][0] + round["extra_scores"][0] for round in rounds
    )
    team_b_total = sum(
        round["scores"][1] + round["extra_scores"][1] for round in rounds
    )

    return team_a_total, team_b_total


@app.callback(
    [Output("mi-zvanja", "children"), Output("vi-zvanja", "children")],
    Input("rounds", "data"),
)
def update_zvanja(rounds: list[Round]) -> tuple[int, int]:
    if rounds == []:
        return 0, 0

    team_a_zvanja = sum(round["extra_scores"][0] for round in rounds)
    team_b_zvanja = sum(round["extra_scores"][1] for round in rounds)

    return team_a_zvanja, team_b_zvanja


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
        extra_points = 90
    else:
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


@app.callback(
    Output("rounds", "data"),
    Output("button-odustani", "n_clicks"),
    [
        Input("button-spremi", "n_clicks"),
    ],
    [
        [State("score_team_a", "data"), State("score_team_b", "data")],
        [State("extra_points_team_a", "data"), State("extra_points_team_b", "data")],
        State("rounds", "data"),
        State("button-odustani", "n_clicks"),
    ],
    prevent_initial_call=True,
)
def save_round(
    n_clicks_save: int,
    scores: tuple[int, int],
    extra_scores: tuple[int, int],
    rounds: list[Round],
    n_clicks: int,
) -> None:
    if sum(scores) == 0:
        return dash.no_update

    round = Round(Team.TEAM_A, Team.TEAM_B, scores, extra_scores)
    rounds.append(round.__dict__)

    return rounds, n_clicks + 1


if __name__ == "__main__":
    app.run(debug=True)
