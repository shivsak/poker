from board import Board
from compare import *
from deck import Deck
import time

def simulate(heroHand, villainHand, numberOfSimulations=1000, currentBoard=None):
	start_time = time.time()

	# run simulations on board to see who would win how many times
	heroWins = 0
	villainWins = 0
	numTies = 0

	for i in range(numberOfSimulations):
		deck = setupDeck(heroHand, villainHand, currentBoard)

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
			if topCard in deck.cards:
				deck.cards.remove(topCard)
		result = compareHands(heroHand, villainHand, board)
		if result == 1:
			heroWins += 1
		elif result == -1:
			villainWins += 1
		else:
			numTies += 1

	printSimulationResults(heroWins, numberOfSimulations, start_time)

	return heroWins/numberOfSimulations, numTies/numberOfSimulations, villainWins/numberOfSimulations

def setupDeck(heroHand, villainHand, currentBoard=None):
	deck = Deck()

	# Remove dealt cards from Deck
	deck.cards.remove(heroHand.card1)
	deck.cards.remove(heroHand.card2)
	deck.cards.remove(villainHand.card1)
	deck.cards.remove(villainHand.card2)

	if currentBoard:
		for card in currentBoard.board:
			deck.cards.remove(card)
	deck.shuffle()
	return deck


# prints simulation results
def printSimulationResults(heroWins, numberOfSimulations, startTime):
	print("hero wins " + str(heroWins) + " times out of " + str(numberOfSimulations))
	print("")
	print("hero has " + str(heroWins * 100 / numberOfSimulations) + "% equity")
	print("")
	print("--- %s seconds ---" % (time.time() - startTime))