from hand_evaluations import *
from parser import *
from simulator import *

from enumerators import *


if __name__ == "__main__":

	heroHand = PlayerHand(Card("A", Suits.SPADES), Card("2", Suits.SPADES))
	villainHand = PlayerHand(Card("6", Suits.CLUBS), Card("7", Suits.CLUBS))
	board = Board(board=(Card("3", Suits.SPADES), Card("4", Suits.SPADES), Card("5", Suits.SPADES)))

	printHand(heroHand)
	printHand(villainHand)
	printCards(board.board)

	heroEquity = simulate(heroHand, villainHand, numberOfSimulations=1000, currentBoard=board)
	print(heroEquity)

	# test("5c2d", "3h5h", "Ks8s5s4s9d")

