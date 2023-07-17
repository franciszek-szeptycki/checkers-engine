import time
from random import randint

from warcaby.pawn import Pawn
from warcaby.utils import is_legal
from warcaby.config import BLACK, WHITE, SIZE


class Board:
    #####################
    #  INITIAL METHODS  #
    #####################

    def __init__(self, board=[]):
        self.board = board
        self.reset_board()
        self.show()

    def reset_board(self):
        for j in range(SIZE):
            for i in range(SIZE):
                if is_legal(i, j):
                    if j < 3:
                        pass
                    elif j > 4:
                        self.board.append(Pawn(self, i, j, BLACK))
        self.board.append(Pawn(self, 7, 3, WHITE))

    ################
    #  FOR HUMANS  #
    ################

    def show(self):
        print(["x"] + [f"{i}" for i in range(SIZE)])
        presented_board = [[' ' for _ in range(SIZE)] for _ in range(SIZE)]

        for pawn in self.board:
            presented_board[pawn.y][pawn.x] = pawn.color

        index = 0
        for row in presented_board:
            print([f"{index}"] + row)
            index += 1

    ##############
    #  GET DATA  #
    ##############

    def get_pawn_list(self, color):
        return [pawn for pawn in self.board if pawn.color == color]

    def get_pawn(self, x, y):
        for pawn in self.board:
            if pawn.x == x and pawn.y == y:
                return pawn

    def get_back_field(self, first_x, first_y, second_x, second_y):
        new_x = 2 * second_x - first_x
        new_y = 2 * second_y - first_y
        pawn = self.get_pawn(new_x, new_y)
        if not pawn and is_legal(new_x, new_y):
            return {"x": new_x, "y": new_y, "victims": [self.get_pawn(second_x, second_y)]}

    #############
    #  ACTIONS  #
    #############

    def remove_pawn(self, pawn):
        self.board = [p for p in self.board if p is not pawn]
