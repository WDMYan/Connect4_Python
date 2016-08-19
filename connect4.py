



def make_board():
	'''
	create a connect4 board. 6 X 7
	@returns: board

	'''
	board = []
	for row_index in range(6):
		row = ['*'] * 7
		board.append(row)
	return board


def display_board(board):
	'''
	display the board with index (both row and column index)
	'''
	i = 5
	for row in board[::-1]:
		print(i, end = ' ')
		for entry in row[:6]:
			print(entry, end = ' ')
		print(row[6])
		i += -1
	print(' ', 0, 1, 2, 3, 4, 5, 6)
	print('\n')
	



def row_win(board):
	'''
	if a row have connected 4 same pattern, then the game end

	'''

	for row in board:
		text = ''.join(row)
		if text.find('OOOO') != -1 or text.find('XXXX') != -1:
			return True
	return False


def transpose(board):
	'''
	transpose the board

	'''
	trans = []#create a new vacant list
	for col_index in range(len(board[0])):
		trans_row = []#create the new row
		for row in board:
			trans_row.append(row[col_index])
		trans.append(trans_row)
	return trans


def column_win(board):
	'''
	use transpose function and row win to check column win

	'''
	trans = transpose(board)
	return(row_win(trans))



def diag_win(board):
	'''
	check if 4 connected as a diagonal line

	'''
	for rowstart in range(0,len(board)-3):
		for columnstart in range(0, len(board[0])-3):
			subboard = []
			for row in board[rowstart:rowstart+4]:
				subrow = row[columnstart:columnstart+4]
				subboard.append(subrow)
			if subboard[0][0] == subboard[1][1] and subboard[1][1] ==subboard[2][2] and subboard[2][2] == subboard[3][3] and (subboard[0][0] == 'X' or subboard[0][0] == 'O'):
				return True
			if subboard[0][3] == subboard[1][2] and subboard[1][2] ==subboard[2][1] and subboard[2][1] == subboard[3][0] and (subboard[3][0] == 'X' or subboard[3][0] == 'O'):
				return True
	return False

def won(board):
	'''
	check if some one win the game
	'''
	return (row_win(board) or column_win(board) or diag_win(board))


def tie(board):
	'''
	check the game get a tie
	'''
	if won(board):
		return False
	for row in board:
		for piece in row:
			if piece == '*':
				return False
	return True


def is_gameover(board):
	'''
	check if the game is over
	returns True and False
	'''
	return (won(board) or tie(board))

def get_move(player):
	'''
	asking for a valid move
	which means an integer from 0-6
	returns the integer of move
	asking for the player-'X' or 'O'
	for the prompt

	'''
	promp = player + ' ' + 'please enter a move: '
	move = ''
	while move not in ['0', '1', '2', '3','4','5','6']:
		move = input(promp).strip()
	return int(move)


def make_move(turn, move, board):
	'''
	make the move on the board, asking input of whose turn and which column to add 
	and the original board

	returns the updated board

	'''
	trans = transpose(board)
	player = 'XO'[turn]
	while '*' not in trans[move]: #deal with the column is full situation
		move = get_move(player)#asking for new input of move

	#normal cases
	if turn % 2 == 0: 
		for row in board:
			if row[move] != '*': 
				continue
			else:
				row[move] = 'X'
				return board
				
	if turn % 2 == 1:
		for row in board:
			if row[move] != '*': 
				continue
			else:
				row[move] = 'O'
				return board


def connect4():

	'''
	main function for the game

	'''
	player = {0:'X', 1:'O'}

	board = make_board()

	turn = 0 #if turn is 0 it is X's turn and if it is 1 it is O's turn

	while not is_gameover(board):
		display_board(board)
		move = get_move(player[turn])
		board = make_move(turn, move, board)
		turn = (turn + 1) % 2

	#game is now over
	#display the board one last time
	display_board(board)

	# declare a winner
	if tie(board):
		print('The game ended in a tie.')
	elif turn == 0:
		print('O won the game.')
	elif turn == 1:
		print('X won the game.')

#play connect 4 game :)
connect4()

	

