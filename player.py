# player.py

from hand import Hand
from card import Card
from enumerators import Suits
from helpers import printPlayerInfo

class Player(object):
	def __init__(self, chips=0, hand=None, name=""):
		self.chips = chips
		self.hand = hand
		self.name = name

	def addChips(self, chipsToAdd):
		self.chips += chipsToAdd

if __name__ == '__main__':
	h = Hand(Card("A", Suits.SPADES), Card("T", Suits.SPADES))
	p = Player(chips=1000, hand=h)
	printPlayerInfo(p)