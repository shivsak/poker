# game.py

from player import Player
from deck import Deck
from dealer import Dealer
from hand import Hand
from helpers import  *
from evaluator import *

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
		print("")
		print("")
		print("")


	# Heads Up Play against Intelligence
	def play(self, player=None):

		#Init Player if none
		if not player:
			player = Player(chips=1000, name="Test Player", position=0)


		#Init intelligence
		intelligence = Player(chips=1000, name="AI", position=0)
		self.players += player,intelligence


		#New Hand
		hand = Hand(self.players, button=self.button)
		board = Board()

		#SB and BB post blinds
		if player.position == hand.button:
			player.chips -= self.SB
			intelligence.chips -= self.BB
		else:
			player.chips -= self.BB
			intelligence.chips -= self.SB

		hand.pot += self.SB + self.BB

		# Dealer deals hand to players
		dealer.dealToPlayers(self.players)

		# Dealer deals flop
		board.cards = dealer.dealFlop()

		printCards(board.cards, title="Flop")

		# Betting round
		playerOption = parseOptionInput(input("Check (c), Bet (b) or Fold (f)"))


		# Dealer deals turn
		board.cards = dealer.dealTurn(board.cards)

		# Betting round

		# Dealer deals river
		board.cards = dealer.dealRiver(board.cards)

		# Betting round



		# Print everyone's cards and hand evaluations

		for player in self.players:
			print(player.name + ": " + player.hand.to_string() + " has a " + str(evaluate(player.hand, board).getEvalString()))

		# Print board
		printCards(board.cards, title="Board")

		# Print Who won and pot size

		print("Pot size: " + str(hand.pot))


	def cards(self):
		return self.board


if __name__ == '__main__':
	Player1 = Player(name="themilkachoc", chips=1000)
	Player2 = Player(name="intelligence", chips=1000)
	players = (Player1,Player2)

	g = Game(0.50, 1)
	deck = Deck()
	dealer = Dealer(deck)

	# Start game
	g.print()


	# new hand - hand number __
	g.play()