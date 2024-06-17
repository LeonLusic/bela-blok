import dash
import dash_bootstrap_components as dbc
from dash import html

dash.register_page(__name__, path="/")


def game_summaries() -> html.Div:
    return html.Div(
        [
            dbc.Row(
                [
                    dbc.Col(
                        [
                            dbc.Badge(
                                "0",
                                id="mi-game-wins",
                                color="success",
                                className="rounded-circle p-2 mb-1",
                            ),
                            html.H2("0", className="mb-0"),
                            html.Div("MI", className="mt-1"),
                        ],
                        className="text-center",
                    ),
                    dbc.Col(
                        [
                            dbc.Badge(
                                "0",
                                id="vi-game-wins",
                                color="danger",
                                className="rounded-circle p-2 mb-1",
                            ),
                            html.H2("0", className="mb-0"),
                            html.Div("VI", className="mt-1"),
                        ],
                        className="text-center",
                    ),
                ],
                justify="around",
                className="mb-3",
            ),
            html.Div(["• " * 9], className="text-center text-muted mb-3"),
            html.Div("Oni su pobijedili", className="text-center text-danger my-3"),
            html.Div(
                dbc.Button(
                    "Poništi zadnju rundu", color="link", className="text-muted"
                ),
                className="text-center mb-3",
            ),
        ]
    )


def current_game_rounds(rounds: list) -> html.Div:
    def round_summary(round: dict) -> dbc.Row:
        return dbc.Row(
            [
                dbc.Col(
                    html.Div(round["score_team_a"], className="text-center mb-2"),
                    className="text-center",
                ),
                dbc.Col(
                    html.Div(
                        html.Img(src="path_to_image", className="icon"),
                        className="text-center mb-2",
                    ),
                    className="text-center",
                ),
                dbc.Col(
                    html.Div(round["score_team_b"], className="text-center mb-2"),
                    className="text-center",
                ),
            ]
        )

    html.Div(
        dbc.Row(
            [round_summary(round) for round in rounds],
            justify="around",
            className="mb-3",
        )
    )


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
            game_summaries(),
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
