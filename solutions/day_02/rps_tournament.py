from solutions.loader.input_loader import load_input_data


class Tile:

    def name(self):
        pass

    def value(self):
        pass

    def check(self, tile):
        pass


class Rock(Tile):

    def name(self):
        return "ROCK"

    def value(self):
        return 1

    def check(self, tile):
        if tile.name() == "ROCK":
            return 3

        if tile.name() == "PAPER":
            return 0

        if tile.name() == "SCISSORS":
            return 6


class Paper(Tile):

    def name(self):
        return "PAPER"

    def value(self):
        return 2

    def check(self, tile):
        if tile.name() == "ROCK":
            return 6

        if tile.name() == "PAPER":
            return 3

        if tile.name() == "SCISSORS":
            return 0


class Scissors(Tile):

    def name(self):
        return "SCISSORS"

    def value(self):
        return 3

    def check(self, tile):
        if tile.name() == "ROCK":
            return 0

        if tile.name() == "PAPER":
            return 6

        if tile.name() == "SCISSORS":
            return 3


tiles = {
    "A": {"tile": Rock(), "defeats": Scissors(), "loses": Paper()},
    "B": {"tile": Paper(), "defeats": Rock(), "loses": Scissors()},
    "C": {"tile": Scissors(), "defeats": Paper(), "loses": Rock()},
    "X": {"tile": Rock(), "defeats": Scissors(), "loses": Paper()},
    "Y": {"tile": Paper(), "defeats": Rock(), "loses": Scissors()},
    "Z": {"tile": Scissors(), "defeats": Paper(), "loses": Rock()},
}


def normal_round(opp_hand, my_hand):
    opp_tile = tiles[opp_hand]["tile"]
    my_tile = tiles[my_hand]["tile"]

    return my_tile.check(opp_tile) + my_tile.value()


def modified_round(opp_hand, my_hand):
    opp_tile = tiles[opp_hand]["tile"]
    my_tile = None

    if my_hand == "Y":
        my_tile = opp_tile

    if my_hand == "X":
        my_tile = tiles[opp_hand]["defeats"]

    if my_hand == "Z":
        my_tile = tiles[opp_hand]["loses"]

    return my_tile.check(opp_tile) + my_tile.value()


class RPSTournament:
    _lines: [str] = []

    def __init__(self, is_example: bool):
        self._lines = load_input_data(2, is_example)

    def run_tournament(self, run_round_fn):
        total_score = 0

        for line in self._lines:
            data = line.split()
            total_score += run_round_fn(data[0], data[1])

        return total_score
