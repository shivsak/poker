# board.py

class Board(object):
	# board is a list of Card objects
	def __init__(self, board):
		self.board = board

	def to_string(self):
		boardString = ""
		for card in self.board:
			boardString += card.to_string() + ", "

		return boardString

	def getSuits(self):
		boardSuits = ()
		for card in self.board:
			boardSuits += (card.suit,)
		return boardSuits

	def cards(self):
		return self.board
