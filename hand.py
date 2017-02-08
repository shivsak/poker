# hand.py

class Hand(object):
	def __init__(self, card1, card2):
		self.card1 = card1
		self.card2 = card2

	def cards(self):
		return self.card1, self.card2

	def getSuits(self):
		return self.card1.suit, self.card2.suit

	def to_string(self):
		return self.card1.to_string() + self.card2.to_string()

	def print(self):
		print(self.to_string())
