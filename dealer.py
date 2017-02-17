# deal.py

from deck import Deck
from helpers import printDeck, printCards
from player import Player

class Dealer(object):
	# constructor
	def __init__(self, deck):
		self.deck = deck
		self.deck.shuffle()

	# takes a list of players
	def dealToPlayers(self, players):

		if (len(players) > 10):
			raise ValueError("Too many players in hand")

		playerCards = []

		i = 0;
		while i <= ((len(players) * 2) -1):
			if i < len(players):
				players[i].hand.card1 = self.deck.dealTopCard()
			else:
				players[i%len(players)].hand.card2 = self.deck.dealTopCard()
			i += 1


	def dealFlop(self):
		# Burn a card
		self.deck.dealTopCard()

		flop = ()
		#Flop:
		for i in range(3):
			flop += (self.deck.dealTopCard(),)

		return flop

# Tester
if __name__ == '__main__':
	deck = Deck()
	deck.shuffle()
	dealer = Dealer(deck)
	print(printDeck(dealer.deck))
	p = Player(name="P2", chips=1000)
	dealer.dealToPlayers((p,))
	print(p.hand.card1.to_string())
	print(p.hand.card2.to_string())
