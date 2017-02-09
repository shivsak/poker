from board import Board
from compare import *
from hand_evaluations import *
from parser import *
from evaluator import evaluate
from enumerators import *
from deck import Deck
import time



def simulate(heroHand, villainHand, numberOfSimulations=1000):
	start_time = time.time()

	# run simulations on board to see who would win how many times
	heroWins = 0
	villainWins = 0
	numTies = 0

	for i in range(numberOfSimulations):
		deck = Deck()
		deck.deck.remove(heroHand.card1)
		deck.deck.remove(heroHand.card2)
		deck.deck.remove(villainHand.card1)
		deck.deck.remove(villainHand.card2)

		# Remove dealt cards from Deck

		deck.shuffle()
		board = Board()
		for j in range(5):
			board.board += (deck.dealTopCard(),)
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

	heroHand = Hand(Card("A", Suits.SPADES), Card("A", Suits.DIAMONDS))
	villainHand = Hand(Card("7", Suits.HEARTS), Card("7", Suits.CLUBS))

	printHand(heroHand)
	printHand(villainHand)

	heroEquity = simulate(heroHand, villainHand, numberOfSimulations=5000)
	print(heroEquity)

	# test("5c2d", "3h5h", "Ks8s5s4s9d")




	# Takes string inputs
def test(heroHandInput, villainHandInput, boardInput):
	heroHand = parseHand(heroHandInput)
	villainHand = parseHand(villainHandInput)
	board = Board(parseBoard(boardInput))

	print("Hero's Hand: " + heroHand.to_string())
	print("Villain's Hand: " + villainHand.to_string())
	print("Board: " + board.to_string())
	print("")
	print("")
	printEvaluations(evaluate(heroHand, board), evaluate(villainHand, board))
	print("")
	print("")

	# Compare Hero Hand and VillainHand
	print("******* COMPARE HANDS *********")
	compareHands(heroHand, villainHand, board)

