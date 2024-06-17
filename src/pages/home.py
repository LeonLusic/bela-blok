import dash
import dash_bootstrap_components as dbc
from dash import html

from components import current_game_rounds, game_summaries

dash.register_page(__name__, path="/")


def layout(**kwargs) -> dbc.Container:
    return dbc.Container(
        [
            dbc.Row(
                [
                    dbc.Col(html.Div("15:08"), width=1),
                    dbc.Col(width=10),
                    dbc.Col(html.Div(html.I(className="bi bi-wifi")), width=1),
                ],
                align="center",
                justify="between",
                className="mb-3",
            ),
            html.Div(["• " * 9], className="text-center text-muted mb-3"),
            dbc.Container(
                current_game_rounds([]),
                id="game-summaries-container",
                style={
                    "min-height": "20vh",
                    "display": "flex",
                    "flex-direction": "column",
                },
            ),
            dbc.Row(
                [
                    dbc.Col(
                        [
                            html.H3("0", id="mi-ukupno", className="text-success"),
                            html.Div("ukupno", className="text-muted"),
                        ],
                        className="text-center",
                    ),
                    dbc.Col(
                        [
                            html.H3("0", id="vi-ukupno", className="text-danger"),
                            html.Div("ukupno", className="text-muted"),
                        ],
                        className="text-center",
                    ),
                ],
                justify="around",
                className="mb-3",
            ),
            dbc.Row(
                [
                    dbc.Col(
                        [
                            html.H3("0", id="mi-zvanja", className="text-success"),
                            html.Div("zvanja", className="text-muted"),
                        ],
                        className="text-center",
                    ),
                    dbc.Col(
                        [
                            html.H3("0", id="vi-zvanja", className="text-danger"),
                            html.Div("zvanja", className="text-muted"),
                        ],
                        className="text-center",
                    ),
                ],
                justify="around",
                className="mb-3",
            ),
            dbc.Row(
                [
                    dbc.Col(
                        [
                            html.H3("0", className="text-success"),
                            html.Div("štiglje", className="text-muted"),
                        ],
                        className="text-center",
                    ),
                    dbc.Col(
                        [
                            html.H3("0", className="text-danger"),
                            html.Div("štiglje", className="text-muted"),
                        ],
                        className="text-center",
                    ),
                ],
                justify="around",
                className="mb-3",
            ),
            dbc.Row(
                [
                    dbc.Col(
                        dbc.Button(
                            "MI", href="scores", color="success", className="btn-block"
                        )
                    ),
                    dbc.Col(
                        dbc.Button(
                            "VI", href="scores", color="danger", className="btn-block"
                        )
                    ),
                ],
                justify="around",
                className="mb-3",
            ),
        ],
        fluid=True,
    )
