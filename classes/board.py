class Board:

    def __init__(self):
        self.matrix = []

    def generate(self, size):
        self.matrix = [['O' for y in range(size)] for x in range(size)]

    def set_robot(self, robot, x, y):
        self.matrix[y][x] = robot

    def display(self):
        for row in self.matrix:
            for val in row:
                print '{:10}'.format(val),
            print
