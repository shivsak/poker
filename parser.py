# parser.py

from card import Card
from hand import Hand

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
