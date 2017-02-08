# compare.py

from poker import evaluate
from win_cases import *

# Compare hero's hand and villain's hand on the current board
def compareHands(heroHand, villainHand, board):
	heroHandEvaluation = evaluate(heroHand, board)
	villainHandEvaluation = evaluate(villainHand, board)

	# printEvaluations(heroHandEvaluation, villainHandEvaluation)

	if (heroHandEvaluation.evaluation.value > villainHandEvaluation.evaluation.value):
		return heroWins()
	elif (heroHandEvaluation.evaluation.value == villainHandEvaluation.evaluation.value):
		if (heroHandEvaluation.highCard > villainHandEvaluation.highCard):
			return heroWins()
		elif (heroHandEvaluation.highCard < villainHandEvaluation.highCard):
			return villainWins()
		elif (heroHandEvaluation.highCard == villainHandEvaluation.highCard):
			if (heroHandEvaluation.secondHighCard > villainHandEvaluation.secondHighCard):
				return heroWins()
			elif (heroHandEvaluation.secondHighCard < villainHandEvaluation.secondHighCard):
				return villainWins()
			else:
				return tie()
	else:
		return villainWins()


def preFlopCompare(heroHand, villainHand):

	return 0
