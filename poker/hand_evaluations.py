# hand_evaluations.py

from poker.enumerators import HandScores
from poker.helpers import *

class HandEvaluation(object):
	def __init__(self, eval, high, secondHigh=0):
		# eval contains an evaluation of the hand
		self.evaluation = eval
		# high contains the high card for straight flushes, flushes, straights, quads, three of a kind, two pairs, pairs and high cards
		self.highCard = high
		# secondHigh contains the 'kicker' or pair in full houses or second pair in two pairs
		self.secondHighCard = secondHigh


	def getEvalRanking(self):
		return 0


	def getHandScore(self):
		self.evaluation.to_string()


	def getEvalString(self):
		if self.evaluation == HandScores.STRAIGHT_FLUSH:
			return "Straight Flush to " + str(getRankString(self.highCard))
		elif self.evaluation == HandScores.QUADS:
			return "Four of a Kind, " + str(getRankString(self.highCard))
		elif self.evaluation == HandScores.FULL_HOUSE:
			return "Full House, " + str(getRankString(self.highCard)) + "s full over " + str(getRankString(self.secondHighCard)) + "s"
		elif self.evaluation == HandScores.FLUSH:
			return "Flush, " + str(getRankString(self.highCard)) + " high"
		elif self.evaluation == HandScores.STRAIGHT:
			return "Straight to " + str(getRankString(self.highCard))
		elif self.evaluation == HandScores.TRIPS:
			return "Three of a Kind, " + str(getRankString(self.highCard))
		elif self.evaluation == HandScores.TWO_PAIR:
			return "Two Pair - " + str(getRankString(self.highCard)) + "s and " + str(getRankString(self.secondHighCard)) + "s"
		elif self.evaluation == HandScores.PAIR:
			return "Pair of " + str(getRankString(self.highCard))
		elif self.evaluation == HandScores.HIGH:
			return "High Card, " + str(getRankString(self.highCard))
		else:
			return "No Hand Evaluation String found"

