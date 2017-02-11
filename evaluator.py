# evaluator.py

from hand_evaluations import *
from helpers import *
from card import *


# Evaluate using Hand1, Board (array of 5 cards)
def evaluate(hand, board):
	# Get ranks of all cards
	ranks = getRanks(hand, board)

	handEval = HandEvaluation(HandScores.HIGH, max(ranks))

	straightFlushEval = straightFlush(hand, board)
	quadsEval = quads(ranks)
	flushEval = flush(hand, board)
	straightEval = straight(ranks)
	tripsEval = trips(ranks)
	twoPairEval = twoPair(ranks)
	pairEval = pair(ranks)

	# Straight Flush
	if straightFlushEval != 0:
		handEval = HandEvaluation(HandScores.STRAIGHT_FLUSH, straightFlushEval)

	# Quads
	elif quadsEval != 0:
		handEval = HandEvaluation(HandScores.QUADS, quadsEval)

	# Boat
	elif tripsEval != 0 and pairEval != 0:
		handEval = HandEvaluation(HandScores.FULL_HOUSE, tripsEval, pairEval)

	# Flush
	elif flushEval != 0:
		handEval = HandEvaluation(HandScores.FLUSH, flushEval)

	# Straigh
	elif straightEval != 0:
		handEval = HandEvaluation(HandScores.STRAIGHT, straightEval)

	# Trips
	elif tripsEval != 0:
		handEval = HandEvaluation(HandScores.TRIPS, tripsEval)

	# Trips
	elif twoPairEval != 0:
		handEval = HandEvaluation(HandScores.TWO_PAIR, twoPairEval[0], twoPairEval[1])

	# Pair
	elif pairEval != 0:
		handEval = HandEvaluation(HandScores.PAIR, pairEval)

	# printHandEvaluation(handEval)

	return handEval

def quads(ranks):

	for rank in ranks:
		if (ranks.count(rank)) == 4:
			return rank

	return 0


def trips(ranks):
	for rank in ranks:
		if (ranks.count(rank)) == 3:
			return rank

	return 0


def twoPair(ranks):
	pairs = ()
	uniqueRanks = set(ranks)
	# print(uniqueRanks)
	for rank in uniqueRanks:
		if (ranks.count(rank) == 2):
			pairs += (rank,)

	if (len(pairs) >= 2):
		pair1, pair2, *rest  = reversed(sorted(pairs))
		return pair1, pair2

	else:
		return 0


def pair(ranks):
	numPairs = 0
	for rank in ranks:
		if (ranks.count(rank)) == 2:
			return rank

	return 0


# returns rank of high card of straight or 0 if no straight
def straight(ranks):
	# can't make a 5 card straight without a 5 or a 10
	sortedRanks = sorted(ranks)
	if 5 in sortedRanks or 10 in sortedRanks:
		# ranks should have at most 7 elements. So if we check sortedRanks[i]-sortedRanks[i+4]
		i = len(sortedRanks)-1
		while i > (len(sortedRanks)-4):
			if sortedRanks[i]-1 in sortedRanks\
					and sortedRanks[i]-2 in sortedRanks \
					and sortedRanks[i]-3 in sortedRanks \
					and sortedRanks[i]-4 in sortedRanks:
				return sortedRanks[i]
			else:
				i -= 1

	# special case for wheel
	if wheel(sortedRanks):
		return 5
	return 0


# returns rank of high card of straight flush or 0 if no straight flush
# Input is a list of 5 or more cards
def straightFlush(hand, board):
	# can't make a 5 card straight without a 5 or a 10
	cards = ()
	cards += hand.cards() + board.cards()
	sortedCards = sortCardsByRank(cards)
	if cardsContainRank(cards, 5) or cardsContainRank(cards, 10):
		# ranks should have at most 7 elements. So if we check sortedRanks[i]-sortedRanks[i+4]
		i = len(sortedCards)-1
		while i > (len(sortedCards)-4):
			# We now know we have a straight with a high of sortedCards[i], now we check if it is a straight flush
			if Card(sortedCards[i].rank, sortedCards[i].suit) in sortedCards and \
				Card(sortedCards[i].rank - 1, sortedCards[i].suit) in sortedCards and \
				Card(sortedCards[i].rank - 2, sortedCards[i].suit) in sortedCards and \
				Card(sortedCards[i].rank - 3, sortedCards[i].suit) in sortedCards and \
				Card(sortedCards[i].rank - 4, sortedCards[i].suit) in sortedCards:
					return sortedCards[i].rank
			i -= 1

	if wheelStraightFlush(hand, board) != 0:
		return 5

	# special case for wheel straight flush
	return 0


def wheelStraightFlush(hand, board):
	# can't make a 5 card straight without a 5 or a 10
	cards = ()
	cards += hand.cards() + board.cards()
	sortedCards = sortCardsByRank(cards)
	if cardsContainRank(cards, 5):
		# ranks should have at most 7 elements. So if we check sortedRanks[i]-sortedRanks[i+4]
		i = len(sortedCards) - 1
		while i > (len(sortedCards) - 4):
			# We now know we have a straight with a high of sortedCards[i], now we check if it is a straight flush
			if Card(14, sortedCards[i].suit) in sortedCards and \
							Card(2, sortedCards[i].suit) in sortedCards and \
							Card(3, sortedCards[i].suit) in sortedCards and \
							Card(4, sortedCards[i].suit) in sortedCards and \
							Card(5, sortedCards[i].suit) in sortedCards:
				return 5
			i -= 1

	# special case for wheel straight flush
	return 0


# The Wheel is a straight from A-5.
def wheel(ranks):
	if 14 in ranks and 2 in ranks and 3 in ranks and 4 in ranks and 5 in ranks:
		return 5
	else:
		return 0


# Checks if hand and board make a flush. Returns highest pocket card of the flushed suit.
def flush(hand, board):
	allSuits = hand.getSuits() + board.getSuits()

	for suit in Suits:
		if allSuits.count(suit) >= 5:
			return findHighestSuitedCardInHand(hand, suit)

	return 0

