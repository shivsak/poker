# enum.py

from enum import Enum

class HandScores(Enum):
	HIGH = 0
	PAIR = 1
	TWO_PAIR = 2
	TRIPS = 3
	STRAIGHT = 4
	FLUSH = 5
	FULL_HOUSE = 6
	QUADS = 7
	STRAIGHT_FLUSH = 8

	def to_string(self):
		if (self == HandScores.HIGH):
			return "High card"
		elif (self == HandScores.PAIR):
			return "Pair"
		elif (self == HandScores.TWO_PAIR):
			return "Two Pair"
		elif (self == HandScores.TRIPS):
			return "Three of a kind"
		elif (self == HandScores.STRAIGHT):
			return "Straight"
		elif (self == HandScores.FLUSH):
			return "Flush"
		elif (self == HandScores.FULL_HOUSE):
			return "Full House"
		elif (self == HandScores.QUADS):
			return "Four of a kind"
		elif (self == HandScores.STRAIGHT_FLUSH):
			return "Straight Flush"



class HandRanks(Enum):
	TEN = 10
	JACK = 11
	QUEEN = 12
	KING = 13
	ACE = 14


class Suits(Enum):
	SPADES = 'Spades'
	CLUBS = 'Clubs'
	HEARTS = 'Hearts'
	DIAMONDS = 'Diamonds'
