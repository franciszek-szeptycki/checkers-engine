from warcaby.config import BLACK, WHITE, SIZE
from warcaby.utils import is_legal


class Pawn:
    def __init__(self, board, x, y, color):
        self.board = board
        self.color = color
        self.x = x
        self.y = y

    def move(self, data):
        self.x = data["x"]
        self.y = data["y"]
        try:
            for victim in data["victims"]:
                self.board.remove_pawn(victim)
        except KeyError:
            pass
        self.board.show()

    def get_moves(self):
        options = [
            {"x": self.x - 1, "y": self.y - 1},
            {"x": self.x - 1, "y": self.y + 1},
            {"x": self.x + 1, "y": self.y - 1},
            {"x": self.x + 1, "y": self.y + 1},
        ]

        # remove out of bands
        options = [o for o in options if is_legal(o["x"], o["y"])]

        # remove going on somebody
        available_moves = []
        for o in options:
            pawn = self.board.get_pawn(o["x"], o["y"])
            if pawn is None:
                available_moves.append(o)
            elif pawn.color is not self.color:
                data = self.board.get_back_field(self.x, self.y, pawn.x, pawn.y)
                if data:
                    available_moves.append(data)

        # remove bad directed moves
        final_moves = []
        for a in available_moves:
            if self.color is WHITE and a["y"] < self.y:
                continue
            if self.color is BLACK and a["y"] > self.y:
                continue
            final_moves.append(a)

        return final_moves
