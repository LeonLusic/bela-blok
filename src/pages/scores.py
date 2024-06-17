import dash
import dash_bootstrap_components as dbc

import components

dash.register_page(__name__)


def layout(**kwargs) -> dbc.Container:
    return dbc.Container(
        [
            components.score_containers(),
            components.sum_containers(),
            components.make_zvanja_input(),
            components.numpad(),
            components.round_select_buttons(),
        ],
        fluid=True,
        style={"max-width": "500px", "margin": "0 auto", "padding": "20px"},
    )
