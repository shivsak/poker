# player.py

from playerhand import PlayerHand
from card import Card
from enumerators import Suits
from helpers import printPlayerInfo

class Player(object):
	def __init__(self, name="", chips=0, position=0, hand=None):
		self.chips = chips
		self.name = name
		self.position = position
		if hand:
			self.hand = hand
		else:
			self.hand = PlayerHand()

	def addChips(self, chipsToAdd):
		self.chips += chipsToAdd

	def stackSize(self):
		return self.chips


if __name__ == '__main__':
	h = PlayerHand(Card("A", Suits.SPADES), Card("T", Suits.SPADES))
	p = Player(chips=1000, hand=h)
	printPlayerInfo(p)