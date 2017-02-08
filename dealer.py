# deal.py

from deck import Deck
from helpers import printDeck, printCards

class Dealer(object):
	# constructor
	def __init__(self):
		self.deck = Deck()
		self.deck.shuffle()

	# takes a list of players
	def dealToPlayers(self, players):

		player1Cards = ()

		i = 0;
		while i < (len(players) * 2):
			player1Cards += (self.deck.dealTopCard(),)
			i += 1

		return player1Cards

# Tester
if __name__ == '__main__':
	dealer = Dealer()
	print(printDeck(dealer.deck))
	printCards(dealer.dealToPlayers(("P1", "P2")))