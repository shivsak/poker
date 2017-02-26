from hand_evaluations import *
from parser import *
from simulator import *

from enumerators import *


if __name__ == "__main__":

	heroHand = parseHand(input("Enter Hero's hand: "))
	villainHand = parseHand(input("Enter Villain's hand: "))
	# board = Board(board=(Card("3", Suits.SPADES), Card("4", Suits.SPADES), Card("5", Suits.SPADES)))

	printHand(heroHand, title="Hero")
	printHand(villainHand, title="Villain")
	# printCards(board.cards, title="Board")

	heroEquity = simulate(heroHand, villainHand, numberOfSimulations=1000)
	print(heroEquity)

	# test("5c2d", "3h5h", "Ks8s5s4s9d")

