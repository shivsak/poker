# game.py

from player import Player
from deck import Deck
from dealer import Dealer
from hand import Hand

class Game(object):
	# board is a list of Card objects
	def __init__(self, smallBlind, bigBlind, players=()):
		self.players = players
		self.SB = smallBlind
		self.BB = bigBlind
		self.button = 0


	def print(self):

		print("Small Blind: " + str(self.SB))
		print("Big Blind: " + str(self.BB))
		print("")
		print("Players:")
		for player in self.players:
			print("- {} ({})\n ".format(player.name, str(player.chips)))


	def play(self):

		#New Hand
		hand = Hand(self.players, button=self.button)

		#SB and BB post blinds
		for player in self.players:
			if self.players.index(player) == 1: # small blind
				player.chips -= self.SB
				hand.pot += self.SB

			elif self.players.index(player) == 2:  # big blind
				player.chips -= self.BB
				hand.pot += self.BB

		# Dealer deals hand to players
		dealer.dealToPlayers(self.players)

		# Dealer deals flop
		dealer.dealFlop()



	def cards(self):
		return self.board


if __name__ == '__main__':
	Player1 = Player(name="themilkachoc", chips=1000)
	Player2 = Player(name="abcd", chips=1000)
	Player3 = Player(name="qwertyuip", chips=1000)
	players = (Player1,Player2,Player3)

	g = Game(0.50, 1, players=players)
	deck = Deck()
	dealer = Dealer(deck)

	# new hand - hand number __
	g.play()
	g.print()