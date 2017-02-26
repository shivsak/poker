# Card.py

from poker.enumerators import *
from poker.helpers import *

# for pretty printing
PRETTY_SUITS = {
    Suits.SPADES:   "\u2660",
	Suits.HEARTS:   "\u2764",
	Suits.DIAMONDS: "\u2666",
	Suits.CLUBS:    "\u2663"
}

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
		elif suit == Suits.SPADES or suit == Suits.CLUBS or suit == Suits.HEARTS or suit == Suits.DIAMONDS:
			self.suit = suit
		else:
			raise ValueError("Invalid card suit input")


		# Get Rank
		if rank == "T" or rank == "t":
			self.rank = 10
		elif rank == "J" or rank == "j":
			self.rank = 11
		elif rank == "Q" or rank == "q":
			self.rank = 12
		elif rank == "K" or rank == "k":
			self.rank = 13
		elif rank == "A" or rank == "a":
			self.rank = 14
		else:
			self.rank = int(rank)

	def to_string(self, pretty=True):
		if pretty:
			return self.to_pretty_string()
		else:
			return "{}{}".format(getRankString(self.rank), self.suit.value[0].lower())

	def print(self, pretty=False):
		if pretty:
			print(self.to_pretty_string())
		else:
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

	def to_pretty_string(self):
		suit = PRETTY_SUITS[self.suit]
		return "{}{}".format(getRankString(self.rank), suit)

	def __eq__(self, other):
		return self.rank == other.rank and self.suit == other.suit


if __name__ == '__main__':
	c1 = Card("2", Suits.SPADES)
	c2 = Card("A", Suits.SPADES)
	print(c1.to_string(True))
	print(c2.to_pretty_string())