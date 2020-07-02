import time
import pprint
import copy

ALIVE = '*'
EMPTY = '_'

height = 12
width = 10

class Square(object):
	def __init__(self, x, y, state):
		self.x = x
		self.y = y
		self.state = state

board = [[Square(x, y, EMPTY) for x in range(width)] for y in range(height)]

# [y][x]
# glider
board[1][2].state = ALIVE
board[2][2].state = ALIVE
board[3][2].state = ALIVE


board[3][1].state = ALIVE
board[2][0].state = ALIVE


def game_logic(state, neighbors):
	"""
	state: ALIVE or EMPTY
	neighbours: int of how many neighbours square has
	    that are alive
	"""
	if state == ALIVE:
		if neighbors < 2:
			return EMPTY          # Die: Too few
		elif neighbors > 3:
			return EMPTY          # Die: Too many
	else:
		if neighbors == 3:
			return ALIVE          # Regenerate
	return state

def get_neighbours(square, board):
	"""
	square: Square object
	board: the board that we are looking at
	returns: int, number of neighbouars square has
	"""
	x = square.x
	y = square.y

	num_neigh = 0

	for up_down in [-1, 0, 1]:
		for left_right in [-1, 0, 1]:
			if up_down == 0 and left_right == 0:
				pass
			else:
				neigh = board[(y + up_down) % height][(x + left_right) % width]
				if neigh.state == ALIVE:
					num_neigh += 1
	return num_neigh

def print_board(board):
	"""
	prints the board nicely
	"""
	b = [[board[y][x].state for x in range(width)] for y in range(height)]
	pprint.pprint(b)

while True:
	print_board(board)
	old_board = copy.deepcopy(board)

	for y in range(height):
		for x in range(width):
			old_state = old_board[y][x].state
			num_neighbours_on_old_board = get_neighbours(old_board[y][x], old_board)
			board[y][x].state = game_logic(old_state, num_neighbours_on_old_board)

	time.sleep(.04)


