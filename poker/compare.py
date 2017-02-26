# compare.py

from poker.evaluator import evaluate
from poker.win_cases import *

# Compare hero's hand and villain's hand on the current board
def compareHands(heroHand, villainHand, board):
	heroHandEvaluation = evaluate(heroHand, board)
	villainHandEvaluation = evaluate(villainHand, board)

	# printEvaluations(heroHandEvaluation, villainHandEvaluation)

	if (heroHandEvaluation.evaluation.value > villainHandEvaluation.evaluation.value):
		return heroWins(heroHandEvaluation)
	elif (heroHandEvaluation.evaluation.value == villainHandEvaluation.evaluation.value):
		if (heroHandEvaluation.highCard > villainHandEvaluation.highCard):
			return heroWins(heroHandEvaluation)
		elif (heroHandEvaluation.highCard < villainHandEvaluation.highCard):
			return villainWins(villainHandEvaluation)
		elif (heroHandEvaluation.highCard == villainHandEvaluation.highCard):
			if (heroHandEvaluation.secondHighCard > villainHandEvaluation.secondHighCard):
				return heroWins(heroHandEvaluation)
			elif (heroHandEvaluation.secondHighCard < villainHandEvaluation.secondHighCard):
				return villainWins(villainHandEvaluation)
			else:
				return tie(heroHandEvaluation)
	else:
		return villainWins(villainHandEvaluation)


def preFlopCompare(heroHand, villainHand):

	return 0
