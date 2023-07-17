def is_legal(x, y):
    if (x + y) % 2 != 0:
        return False
    if x < 0 or x > 7 or y < 0 or y > 7:
        return False
    return True
