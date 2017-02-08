from collections import Counter
from enum import Enum

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
	compare(heroHand, villainHand, board)


# Parse the board
def parseBoard(boardInput):
	if len(boardInput)%2 != 0:
		raise ValueError("incorrect board input")
	handList = list(boardInput)

	board = ()

	i = 0
	while i < len(boardInput):
		card = Card(handList[i], handList[i+1])
		board += (card,)

		i+=2

	return board


def printHandEvaluation(handEvaluation):
	print(handEvaluation.getEvalString())


# Evaluate using Hand1, Board (array of 5 cards)
def evaluate(hand, board):
	# Get ranks of all cards
	ranks = getRanks(hand, board)

	handEval = HandEvaluation(HandScores.HIGH, max(ranks))

	quadsEval = quads(ranks)
	flushEval = flush(hand, board)
	straightEval = straight(ranks)
	tripsEval = trips(ranks)
	twoPairEval = twoPair(ranks)
	pairEval = pair(ranks)

	# Quads
	if quadsEval != 0:
		handEval = HandEvaluation(HandScores.QUADS, quadsEval)

	# Boat
	elif tripsEval != 0 and pairEval != 0:
		handEval = HandEvaluation(HandScores.FULL_HOUSE, tripsEval, pairEval)

	# Flush
	elif flushEval != 0:
		handEval = HandEvaluation(HandScores.FLUSH, flushEval)

	# Straight
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
	print(uniqueRanks)
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


def findHighestSuitedCardInHand(hand, suit):
	highestRank = 0
	if hand.card1.suit == suit:
		highestRank = hand.card1.rank
		if hand.card2.suit == suit and hand.card2.rank > hand.card1.rank:
			highestRank = hand.card2.rank
	else:
		if hand.card2.suit == suit:
			highestRank = hand.card2.rank

	return highestRank


# Takes a list of Suit objects and prints the suits
def printSuits(suits):
	for suit in suits:
		print(suit.value, end=" ")
	print("")


# get ranks of all 7 cards
def getRanks(hand, board):
	inputCards = hand.cards() + board.cards()
	cards = []
	for card in inputCards:
		cards.append(card.getNumericalRank())

	return cards


# Parse Card
# Card must be entered as AsKs, 6d7h, etc
def parseCard(card):
	if len(card) > 2:
		raise ValueError("incorrect card input")
	cardArray = list(card)

	card = Card(cardArray[0], cardArray[1])
	card.print()


# Parse Hand
def parseHand(hand):
	if len(hand) != 4:
		raise ValueError("incorrect hand input")
	handList = list(hand)

	card1 = Card(handList[0], handList[1])
	card2 = Card(handList[2], handList[3])
	return Hand(card1, card2)


class Hand(object):
	def __init__(self, card1, card2):
		self.card1 = card1
		self.card2 = card2

	def cards(self):
		return self.card1, self.card2

	def getSuits(self):
		return self.card1.suit, self.card2.suit

	def to_string(self):
		return self.card1.to_string() + self.card2.to_string()

	def print(self):
		print(self.to_string())


def getRankString(rank):
	if rank == 10:
		return 'T'
	if rank == 11:
		return 'J'
	elif rank == 12:
		return 'Q'
	elif rank == 13:
		return 'K'
	elif rank == 14:
		return 'A'
	else:
		return str(rank)


class Card(object):
	def __init__(self, rank, suit):
		if suit == 's':
			self.suit = Suits.SPADES
		elif suit == 'c':
			self.suit = Suits.CLUBS
		elif suit == 'h':
			self.suit = Suits.HEARTS
		elif suit == 'd':
			self.suit = Suits.DIAMONDS
		else:
			raise ValueError("Invalid card suit input")

		self.rank = rank

	def to_string(self):
		return "{}{}".format(self.rank, self.suit.value[0].lower())

	def print(self):
		print(self.to_string())

	def getNumericalRank(self):
		if self.rank == 'T':
			return 10
		if self.rank == 'J':
			return 11
		elif self.rank == 'Q':
			return 12
		elif self.rank == 'K':
			return 13
		elif self.rank == 'A':
			return 14
		else:
			return int(self.rank)

	def getSuit(self):
		return self.suit


class Board(object):
	# board is a list of Card objects
	def __init__(self, board):
		self.board = board

	def to_string(self):
		boardString = ""
		for card in self.board:
			boardString += card.to_string() + ", "

		return boardString

	def getSuits(self):
		boardSuits = ()
		for card in self.board:
			boardSuits += (card.suit,)
		return boardSuits

	def cards(self):
		return self.board


class Deck(object):
	def __init__(self):
		# Array of 52 Card objects
		ranks = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
		suits = ['s', 'c', 'h', 'd']
		self.deck = []

		for rank in ranks:
			for suit in suits:
				self.deck.append(Card(rank, suit))

	def print(self):
		for card in self.deck:
			print(card.to_string(), end=" ")


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



"""
Methods for Comparisons between different hands
"""

# Debugging method to print the hand evaluations
def printEvaluations(heroHandEvaluation, villainHandEvaluation):
	print("")
	print("***************")
	print("EVALUATIONS:")
	print("Hero's hand evaluates to " + heroHandEvaluation.getEvalString())
	print("Villain's hand evaluates to " + villainHandEvaluation.getEvalString())
	print("***************")
	print("")


# Compare hero's hand and villain's hand on the current board
def compare(heroHand, villainHand, board):
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
			tie()
	else:
		villainWins()


def heroWins():
	print("Hero wins")


def villainWins():
	print("Villain wins")

def tie():
	print("Tie")


class HandScores(Enum):
	HIGH = 0
	PAIR = 1
	TWO_PAIR = 2
	TRIPS = 3
	STRAIGHT = 4
	FLUSH = 5
	FULL_HOUSE = 6
	QUADS = 7
	STRAIGHT_FLUSH = 8

	def to_string(self):
		if (self == HandScores.HIGH):
			return "High card"
		elif (self == HandScores.PAIR):
			return "Pair"
		elif (self == HandScores.TWO_PAIR):
			return "Two Pair"
		elif (self == HandScores.TRIPS):
			return "Three of a kind"
		elif (self == HandScores.STRAIGHT):
			return "Straight"
		elif (self == HandScores.FLUSH):
			return "Flush"
		elif (self == HandScores.FULL_HOUSE):
			return "Full House"
		elif (self == HandScores.QUADS):
			return "Four of a kind"
		elif (self == HandScores.STRAIGHT_FLUSH):
			return "Straight Flush"



class HandRanks(Enum):
	TEN = 10
	JACK = 11
	QUEEN = 12
	KING = 13
	ACE = 14


class Suits(Enum):
	SPADES = 'Spades'
	CLUBS = 'Clubs'
	HEARTS = 'Hearts'
	DIAMONDS = 'Diamonds'

if __name__ == "__main__":
	test("3c8d", "4d2h", "Ks2s3s4sKd")