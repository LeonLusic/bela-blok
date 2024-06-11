class Player:
    def __init__(self, id: str, name: str) -> None:
        self.id = id
        self.name = name


class Card:
    def __init__(self, id: str, value: str, suit: str) -> None:
        self.id = id
        self.value = value
        self.suit = suit


class Round:
    def __init__(self, id: str) -> None:
        self.id = id

    def score(self) -> int:
        raise NotImplementedError


class Game:
    def __init__(self, id: str) -> None:
        self.id = id
        self.rounds: list[Round] = []

    def add_players(self, players: list[Player]) -> None:
        self.players = players

    def add_round(self, round: Round) -> None:
        self.rounds.append(round)

    def _calculate_score(self) -> int:
        return sum(round.score() for round in self.rounds)
