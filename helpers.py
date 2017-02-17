# helpers.py

# Debugging method to print the hand evaluations
def printEvaluations(heroHandEvaluation, villainHandEvaluation):
	print("")
	print("***************")
	print("EVALUATIONS:")
	print("Hero's hand evaluates to " + heroHandEvaluation.getEvalString())
	print("Villain's hand evaluates to " + villainHandEvaluation.getEvalString())
	print("***************")
	print("")


# Get the string value of a hand's rank
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


# Finds highest card of a given suit in a player's hand
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


# get ranks from a list of cards
def getRanksFromCards(inputCards):
	cards = []
	for card in inputCards:
		cards.append(card.getNumericalRank())

	return cards


# prints the hand evaluation string
def printHandEvaluation(handEvaluation):
	print(handEvaluation.getEvalString())


#print the Deck as it is currently
def printDeck(deck, pretty=True):
	print("")
	print("******** DECK *********")
	for card in deck.cards:
		print (card.to_string(pretty=pretty), end=" ")
	print("")
	print("***********************")
	print("")


# prints a given Hand
def printHand(hand, pretty=True):
	cards = hand.card1, hand.card2
	printCards(cards, pretty=pretty)

# print a list of Card objects
def printCards(cards, pretty=True):
	print("")
	print("******** Cards *********")
	for card in cards:
		print (card.to_string(pretty=pretty), end=" ")
	print("")
	print("***********************")
	print("")


def printPlayerInfo(player):
	print("")
	print("******** Player *********")
	if player.name:
		print("Name: " + str(player.name))
	if player.chips >= 0:
		print("Chips: " + str(player.chips))
	if player.hand:
		print("Hand: " + str(player.hand.to_string(pretty=True)))
	print("***********************")
	print("")


def cardsContainRank(cards, rank):
	for card in cards:
		if card.rank == int(rank):
			return True
	return False

def sortCardsByRank(cards, ascending=True):
	return sorted(cards, key=lambda x: x.rank)

