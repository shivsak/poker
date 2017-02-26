from poker.board import Board
from poker.compare import *
from poker.deck import Deck
from poker.enumerators import *
import time

def simulate(heroHand, villainHand, numberOfSimulations=1000, currentBoard=None, debug=False):
	start_time = time.time()

	# run simulations on board to see who would win how many times
	heroWins = 0
	villainWins = 0
	numTies = 0

	results = {}
	results["heroWins"] = {}
	results["villainWins"] = {}
	results["tie"] = {}

	results["heroWins"]["total"] = 0
	results["villainWins"]["total"] = 0
	results["tie"]["total"] = 0

	for handScore in HandScores:
		results["heroWins"][handScore.to_string()] = 0
		results["villainWins"][handScore.to_string()] = 0
		results["tie"][handScore.to_string()] = 0


	for i in range(numberOfSimulations):
		deck = setupDeck(heroHand, villainHand, currentBoard)

		numCardsToDeal = 5
		if currentBoard:
			if len(currentBoard.cards) == 3:
				board = Board()
				board.cards += currentBoard.cards
				numCardsToDeal = 2
			elif len(currentBoard.cards) == 4:
				board = Board()
				board.cards += currentBoard.cards
				numCardsToDeal = 1
			else:
				raise ValueError("Incorrect flop input")
		else:
			board = Board()


		for j in range(numCardsToDeal):
			topCard = deck.dealTopCard()
			board.cards += (topCard,)
			if topCard in deck.cards:
				deck.cards.remove(topCard)
		result = compareHands(heroHand, villainHand, board)
		if result[0] == 1:
			heroHandEval = result[1]
			results["heroWins"]["total"] += 1
			results["heroWins"][heroHandEval.evaluation.to_string()] += 1
		elif result[0] == -1:
			villainHandEval = result[1]
			results["villainWins"]["total"] += 1
			results["villainWins"][villainHandEval.evaluation.to_string()] += 1
		else:
			heroHandEval = result[1]
			results["tie"]["total"] += 1
			results["tie"][heroHandEval.evaluation.to_string()] += 1

	if debug:
		printSimulationResults(results["heroWins"]["total"], numberOfSimulations, start_time)

	for k in results:
		if k == "\n\nheroWins":
			print("Hero wins by:")
			for e in results[k]:
				print(e + ": " + str(results[k][e]))
		elif k == "villainWins":
			print("\n\nVillain wins by:")
			for e in results[k]:
				print(e + ": " + str(results[k][e]))
		else:
			print("\n\nTie by:")
			for e in results[k]:
				print(e + ": " + str(results[k][e]))

	return results

def setupDeck(heroHand, villainHand, currentBoard=None):
	deck = Deck()

	# Remove dealt cards from Deck
	deck.cards.remove(heroHand.card1)
	deck.cards.remove(heroHand.card2)
	deck.cards.remove(villainHand.card1)
	deck.cards.remove(villainHand.card2)

	if currentBoard:
		for card in currentBoard.cards:
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