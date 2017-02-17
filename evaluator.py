# evaluator.py

from hand_evaluations import *
from helpers import *
from card import *
from board import Board
from playerhand import PlayerHand


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


"""
These methods evaluate things that are not obvious
"""

def quadded(board):
	if len(board.board) < 4:
		return False
	else:
		return quads(getRanksFromCards(board.cards()))


def tripped(board):
	if len(board.board) < 3:
		return False
	else:
		return trips(getRanksFromCards(board.cards())) != 0


def doublePaired(board):
	if len(board.board) < 4:
		return False
	else:
		return twoPair(getRanksFromCards(board.cards())) != 0


def paired(board):
	if len(board.board) < 2:
		return False
	else:
		return pair(getRanksFromCards(board.cards())) != 0

def fourFlushed(board):
	if len(board.board) < 4:
		return False
	else:
		boardSuits = board.getSuits()
		for suit in Suits:
			if boardSuits.count(suit) == 4:
				return True


def fiveFlushed(board):
	if len(board.board) < 5:
		return False
	else:
		boardSuits = board.getSuits()
		for suit in Suits:
			if boardSuits.count(suit) == 5:
				return True


def threeFlushed(board):
	if len(board.board) < 3:
		return False
	else:
		boardSuits = board.getSuits()
		for suit in Suits:
			if boardSuits.count(suit) == 3:
				return True

def straighted(board):
	if len(board.board) < 3:
		return 0
	else:
		sortedRanks = sorted(list(map(lambda x: x.rank, board.board)))
		i = len(sortedRanks)-1
		numberOfConnectedCards = 0
		while i>0:
			if sortedRanks[i] - 1 in sortedRanks and \
				sortedRanks[i] - 2 in sortedRanks and \
				sortedRanks[i] - 3 in sortedRanks and \
				sortedRanks[i] - 4 in sortedRanks:
					numberOfConnectedCards = max(numberOfConnectedCards, 5)
			elif sortedRanks[i] - 1 in sortedRanks and \
					sortedRanks[i] - 2 in sortedRanks and \
					sortedRanks[i] - 3 in sortedRanks:
					numberOfConnectedCards = max(numberOfConnectedCards, 4)
			elif sortedRanks[i] - 1 in sortedRanks and \
					sortedRanks[i] - 2 in sortedRanks and \
					sortedRanks[i] - 3 in sortedRanks:
					numberOfConnectedCards = max(numberOfConnectedCards, 3)
			else:
				numberOfConnectedCards = max(numberOfConnectedCards, 0)

			print(sortedRanks[i])
			i -= 1

		wheel = wheeled(board)

		return max(numberOfConnectedCards, wheel)


def wheeled(board):
	if len(board.board) < 3:
		return 0
	else:
		sortedRanks = sorted(list(map(lambda x: x.rank, board.board)))

		if 14 in sortedRanks and 2 in sortedRanks and 3 in sortedRanks and 4 in sortedRanks and 5 in sortedRanks:
			return 5
		if 14 in sortedRanks and 2 in sortedRanks and 3 in sortedRanks and 4 in sortedRanks:
			return 4
		if 14 in sortedRanks and 2 in sortedRanks and 3 in sortedRanks:
			return 3

	return 0


		# evaluate board texture
def boardTexture(board):
	textures = ()

	# Quads
	quads = quadded(board)
	trips = tripped(board)
	doublePair = doublePaired(board)
	pair = paired(board)
	fourFlush = fourFlushed(board)
	threeFlush = threeFlushed(board)
	fiveFlush = fiveFlushed(board)
	straight = straighted(board)

	if quads:
		textures += (Texture.QUADDED,)

	# Tripped
	if trips:
		textures += (Texture.TRIPPED,)

	# Double Paired
	if doublePair:
		textures += (Texture.DOUBLE_PAIRED,)

	# Paired
	if pair and not doublePair:
		textures += (Texture.PAIRED,)

	# Four flush
	if fiveFlush:
		textures += (Texture.FIVE_FLUSHED,)

	# Four flush
	if fourFlush:
		textures += (Texture.FOUR_FLUSH,)

	# Four flush
	if threeFlush:
		textures += (Texture.THREE_FLUSH,)

	# Three flush
	if not (threeFlush or fourFlush or fiveFlush):
		textures += (Texture.RAINBOW,)

	# Straight
	if straight == 5:
		textures += (Texture.FIVE_STRAIGHT,)
	elif straight == 4:
		textures += (Texture.FOUR_CONNECTED,)
	elif straight == 3:
		textures += (Texture.THREE_CONNECTED,)


	return textures


if __name__ == '__main__':
	board = Board((Card("A", Suits.SPADES), Card("2", Suits.SPADES), Card("3", Suits.SPADES), Card("5", Suits.SPADES), Card("6", Suits.SPADES)))
	print(list(map(lambda x: x.value, boardTexture(board))))