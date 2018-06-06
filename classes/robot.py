class Robot:

    def __init__(self, symbol, x, y):
        self.symbol = symbol
        self.x = x
        self.y = y

    def walk(self, move, step, board_size):
        if move == 'DE':
            self.x += step if (self.x + step < board_size) else 0
        elif move == 'IZ':
            self.x -= step if (self.x > 0) else 0
        elif move == 'AB':
            self.y += step if (self.y + step < board_size) else 0
        elif move == 'AR':
            self.y -= step if (self.y > 0) else 0
        else:
            self.x, self.y = self.x, self.y

    def print_position(self):
        print(self.x, self.y)
