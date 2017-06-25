
print "Welcome to the game of fifteen! To start, enter the dimensions of the board. For example, enter 3 for a 3x3 board."
max_dim = int(raw_input("Size of board: "))



def init(max_dim):

	board = [[0 for x in range(0, max_dim)] for y in range(0, max_dim)]

	val_counter = (max_dim * max_dim) - 1
	
	for i in range(0, max_dim):
		for j in range(0, max_dim):
			board[i][j] = val_counter
			val_counter -= 1

	if max_dim % 2 == 0:
		board[max_dim - 1][max_dim - 2] = 2
		board[max_dim - 1][max_dim - 3] = 1
	return board


def draw(board):

	for i in board:
		for j in i:
			if j == 0:
				print ' _'
			else:
				print '{:2}'.format(j),
		print

def move(board):

	draw(board)

	position = board[max_dim - 1][max_dim - 1]

	num_to_move = int(raw_input("Input number to move: "))

	
board = init(max_dim)
draw(board)
