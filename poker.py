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
	print("Hero's hand evaluates to: " + evaluate(heroHand, board))


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

# Evaluate using Hand1, Board (array of 5 cards)
def evaluate(hand, board):
	# Get ranks of all cards
	ranks = getRanks(hand, board)

	handEval = HandEvaluation(HandScores.HIGH, max(ranks))
	handEvalPrint = ""

	# Quads
	quadsEval = quads(ranks)
	tripsEval = trips(ranks)
	pairEval = pair(ranks)

	# Quads
	if quadsEval != 0:
		handEval = HandEvaluation(HandScores.QUADS, quadsEval)

	# Boat
	elif tripsEval != 0 and pairEval != 0:
		handEval = HandEvaluation(HandScores.FULL_HOUSE, tripsEval, pairEval)

	# Trips
	elif tripsEval != 0:
		handEval = HandEvaluation(HandScores.TRIPS, tripsEval)
	# Pair
	elif pairEval != 0:
		handEval = HandEvaluation(HandScores.PAIR, pairEval)

	handEvalPrint = handEval.getEvalString()

	return handEvalPrint

def quads(ranks):

	for rank in ranks:
		if (ranks.count(rank)) == 4:
			return rank

	return 0


def pair(ranks):
	for rank in ranks:
		if (ranks.count(rank)) == 2:
			return rank

	return 0



def trips(ranks):
	for rank in ranks:
		if (ranks.count(rank)) == 3:
			return rank

	return 0




# get ranks of all 7 cards
def getRanks(hand, board):
	inputCards = hand.cards() + board.cards()
	cards = ()
	for card in inputCards:
		cards += (card.getNumericalRank(),)

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
		return (self.card1, self.card2)

	def to_string(self):
		return self.card1.to_string() + self.card2.to_string()

	def print(self):
		print(self.to_string())


def getRankString(rank):
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
			self.suit = 'SPADES'
		elif suit == 'c':
			self.suit = 'CLUBS'
		elif suit == 'h':
			self.suit = 'HEARTS'
		elif suit == 'd':
			self.suit = 'DIAMONDS'
		else:
			raise ValueError("Invalid card suit input")

		self.rank = rank

	def to_string(self):
		return "{}{}".format(self.rank, self.suit[0].lower())

	def print(self):
		print(self.to_string())

	def getNumericalRank(self):
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

class Board(object):
	# board is a list of Card objects
	def __init__(self, board):
		self.board = board

	def to_string(self):
		boardString = ""
		for card in self.board:
			boardString += card.to_string() + ", "

		return boardString

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


class HandEvaluation():
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


if __name__ == "__main__":
	test("AsAh", "AdAc", "Ac6c6h")