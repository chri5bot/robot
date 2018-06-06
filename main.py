from classes.board import Board
from classes.robot import Robot

f = open('list_moves.txt')

list_moves_from_file = [line.rstrip('\n').split(",") for line in f]

board_size = 5
step = 1

for moves in list_moves_from_file:
    print(moves)
    board = Board()
    board.generate(board_size)
    robot = Robot('ROBOT', 0, 0)
    robot.print_position()
    for move in moves:
        board.set_robot('O', robot.x, robot.y)
        robot.walk(move, step, board_size)
        robot.print_position()
        board.set_robot(robot.symbol, robot.x, robot.y)
    board.display()
