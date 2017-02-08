# Card.py

from enumerators import Suits

class Card(object):
	def __init__(self, rank, suit):
		if suit == 's':
			self.suit = Suits.SPADES
		elif suit == 'c':
			self.suit = Suits.CLUBS
		elif suit == 'h':
			self.suit = Suits.HEARTS
		elif suit == 'd':
			self.suit = Suits.DIAMONDS
		else:
			raise ValueError("Invalid card suit input")

		self.rank = rank

	def to_string(self):
		return "{}{}".format(self.rank, self.suit.value[0].lower())

	def print(self):
		print(self.to_string())

	def getNumericalRank(self):
		if self.rank == 'T':
			return 10
		if self.rank == 'J':
			return 11
		elif self.rank == 'Q':
			return 12
		elif self.rank == 'K':
			return 13
		elif self.rank == 'A':
			return 14
		else:
			return int(self.rank)

	def getSuit(self):
		return self.suit


