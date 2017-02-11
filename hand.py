# hand.py

import random
from enumerators import Suits
from card import Card

class Hand(object):
	def __init__(self, card1=None, card2=None):
		if card1:
			self.card1 = card1
		else:
			self.card1 = Card(2 + int(random.random() * 15), random.choice(list(Suits)))

		if card2:
			self.card2 = card2
		else:
			self.card2 = Card(2 + int(random.random() * 15), random.choice(list(Suits)))


	def cards(self):
		return self.card1, self.card2

	def getSuits(self):
		return self.card1.suit, self.card2.suit

	def to_string(self, pretty=True):
		return self.card1.to_string(pretty=pretty) + self.card2.to_string(pretty=pretty)

	def print(self):
		print(self.to_string())
