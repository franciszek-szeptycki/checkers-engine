from warcaby.board import Board
from warcaby.config import BLACK, WHITE
from random import randint

if __name__ == "__main__":
    game = Board()

    # x = int(input("x: "))
    # y = int(input("y: "))
    x = 5
    y = 5
    my_pawn = game.get_pawn(x, y)
    moves = my_pawn.get_moves()
    for i in range(len(moves)):
        print(f"id: {i} -> {moves[i]}")
    move_id = int(input("option: "))
    my_pawn.move(moves[move_id])

    enemy_pawn = game.get_pawn(7, 3)
    enemy_moves = enemy_pawn.get_moves()
    enemy_move = enemy_moves[randint(0, len(enemy_moves) - 1)]
    enemy_pawn.move(enemy_move)


