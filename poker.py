from board import Board
from compare import *
from hand_evaluations import *
from parser import *
from evaluator import evaluate

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


if __name__ == "__main__":
	test("5c2d", "3h5h", "Ks8s5s4s9d")