# compare.py

from poker import evaluate
from win_cases import *

# Compare hero's hand and villain's hand on the current board
def compareHands(heroHand, villainHand, board):
	heroHandEvaluation = evaluate(heroHand, board)
	villainHandEvaluation = evaluate(villainHand, board)

	# printEvaluations(heroHandEvaluation, villainHandEvaluation)

	if (heroHandEvaluation.evaluation.value > villainHandEvaluation.evaluation.value):
		heroWins()
	elif (heroHandEvaluation.evaluation.value == villainHandEvaluation.evaluation.value):
		if (heroHandEvaluation.highCard > villainHandEvaluation.highCard):
			heroWins()
		elif (heroHandEvaluation.highCard < villainHandEvaluation.highCard):
			villainWins()
		elif (heroHandEvaluation.highCard == villainHandEvaluation.highCard):
			if (heroHandEvaluation.secondHighCard > villainHandEvaluation.secondHighCard):
				heroWins()
			elif (heroHandEvaluation.secondHighCard < villainHandEvaluation.secondHighCard):
				villainWins()
			else:
				tie()
	else:
		villainWins()


def preFlopCompare(heroHand, villainHand):

	return 0
