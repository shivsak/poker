# hand.py

from helpers import *
from board import Board

class Hand():
	def __init__(self, players, button=0, pot=0, board=Board()):
		self.players = players
		self.button = button
		self.pot = pot
		self.board = board


	def printHand(self):
		print("Players:")
		for player in self.players:
			print("- {}: {}{} ({})\n ".format(player.name, player.hand.card1.to_string(), player.hand.card2.to_string(), str(player.chips)))

		print("")
		print("Board:")
		printCards(self.board.cards)