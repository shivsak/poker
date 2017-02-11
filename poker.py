from board import Board
from compare import *
from hand_evaluations import *
from parser import *
from evaluator import evaluate
from enumerators import *
from deck import Deck
import time



def simulate(heroHand, villainHand, numberOfSimulations=1000, currentBoard=None):
	start_time = time.time()

	# run simulations on board to see who would win how many times
	heroWins = 0
	villainWins = 0
	numTies = 0

	for i in range(numberOfSimulations):
		deck = Deck()

		# Remove dealt cards from Deck
		deck.deck.remove(heroHand.card1)
		deck.deck.remove(heroHand.card2)
		deck.deck.remove(villainHand.card1)
		deck.deck.remove(villainHand.card2)

		if currentBoard:
			for card in currentBoard.board:
				deck.deck.remove(card)
		deck.shuffle()

		numCardsToDeal = 5
		if currentBoard:
			if len(currentBoard.board) == 3:
				board = Board()
				board.board += currentBoard.board
				numCardsToDeal = 2
			elif len(currentBoard.board) == 4:
				board = Board()
				board.board += currentBoard.board
				numCardsToDeal = 1
			else:
				raise ValueError("Incorrect flop input")
		else:
			board = Board()


		for j in range(numCardsToDeal):
			topCard = deck.dealTopCard()
			board.board += (topCard,)
			if topCard in deck.deck:
				deck.deck.remove(topCard)
		result = compareHands(heroHand, villainHand, board)
		if result == 1:
			heroWins += 1
		elif result == -1:
			villainWins += 1
		else:
			numTies += 1

	print("hero wins " + str(heroWins) + " times out of " + str(numberOfSimulations))
	print("")
	print("hero has " + str(heroWins * 100 / numberOfSimulations) + " equity")
	print("")
	print("--- %s seconds ---" % (time.time() - start_time))

	return heroWins/numberOfSimulations, numTies/numberOfSimulations, villainWins/numberOfSimulations




if __name__ == "__main__":

	heroHand = Hand(Card("A", Suits.SPADES), Card("2", Suits.SPADES))
	villainHand = Hand(Card("6", Suits.SPADES), Card("7", Suits.CLUBS))
	board = Board(board=(Card("3", Suits.SPADES), Card("4", Suits.SPADES), Card("5", Suits.SPADES)))

	printHand(heroHand)
	printHand(villainHand)
	printCards(board.board)

	heroEquity = simulate(heroHand, villainHand, numberOfSimulations=1000, currentBoard=board)
	print(heroEquity)

	# test("5c2d", "3h5h", "Ks8s5s4s9d")

