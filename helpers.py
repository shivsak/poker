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


# prints the hand evaluation string
def printHandEvaluation(handEvaluation):
	print(handEvaluation.getEvalString())


#print the Deck as it is currently
def printDeck(deck):
	print("")
	print("******** DECK *********")
	for card in deck.deck:
		print (card.to_string(), end=" ")
	print("")
	print("***********************")
	print("")
