# deck.py

import random
from card import Card
from helpers import printDeck

class Deck(object):
	def __init__(self):
		# Array of 52 Card objects
		ranks = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
		suits = ['s', 'c', 'h', 'd']
		self.cards = []

		for rank in ranks:
			for suit in suits:
				self.cards.append(Card(rank, suit))

	def print(self):
		for card in self.cards:
			print(card.to_string(), end=" ")

	# Using Fisher-Yates Algorithm to shuffle the deck
	# source: http://code.activestate.com/recipes/360461-fisher-yates-shuffle/
	def shuffle(self):
		a = len(self.cards)
		b = a - 1
		for d in range(b, 0, -1):
			e = random.randint(0, d)
			if e == d:
				continue
			self.cards[d], self.cards[e] = self.cards[e], self.cards[d]
		return self.cards

	def dealTopCard(self):
		return self.cards.pop()

	def addCardToDeck(self, card):
		self.cards.append(card)


if __name__ == "__main__":
	d = Deck()
	d.shuffle()
	printDeck(d)

	print(d.dealTopCard().to_string())