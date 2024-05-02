from globals import *
import time

#	TODO: use card.parent
def select(selection, multiple=False):
	if isinstance(selection, Card):

		selectedCard = selection

		#	find containing stack
		found = False
		tempCards = []
		for stack in playStacks:
			for card in stack:
				if !found & card == selectedCard:
					found = True
				if found:
					tempCards + card
			for i in tempCards:
				stack.pop()
		for stack in homeStacks:
			for card in stack:
				if card == selectedCard:
					tempCards + card
					stack.pop()
		if waste[-1] == selectedCard:

		tempStack = Stack(tempCards)

	elif isinstance(selection, Stack):
		selectedStack = selection
	else:
		selectedCard = None

def checkWon():
	for stack in playStacks:
		if stack:
			return False
	if stock:
		return False
	if waste:
		return False
	for stack in homeStacks:
		if len(stack) < 13:
			return False
	endTime = time.time()
	return True

def gameTime():
	if gameState == State('start'):
		return 0
	if gameState == State('play'):
		return time.time() - startTime
	if gameState == State('won'):
		return endTime - startTime

def startGame():
	for s in allStacks:
		s.dump()

	#	generate new deck, shuffle, and deal
	deck = Stack(newDeck = True)
	deck.shuffle()

	#	for playstack number n, deal n cards. Flip the topmost card faceup
	for i in range(len(playStacks)):
		for j in range(i+1):
			playStacks[i].append(deck.pop())
		playStacks[i].move(i*playStacks[i][0].width)
		playStacks[i].tidy()
		playStacks[i][-1].flip()
	for c in deck:
		stock.append(deck.pop())

	gameState = State('play')
	startTime = time.time()
	moves = 0
	score = 0

#	testing
# for s in playStacks:
# 	print(s)

#	author: Narbeh Malekian
