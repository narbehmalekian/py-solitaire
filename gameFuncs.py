from globals import *
import time

def moveSelection(dest):
	global score
	global moves
	if (dest == waste) & (originStack == stock):
		waste.append(stock[-1])
		stock.pop()
		waste[-1].flip()
		score += points['hand']
		moves += 1
		print(score)
	elif dest.checkRule(dest, originStack.selected[0]):
		for card in originStack.selected:
			dest + card
			originStack.pop()
			score += points['move']
			if dest in homeStacks:
				score += points['home']
			moves += 1
	else:
		print('invalid move')
	deselect()

def deselect():
	global originStack
	originStack = None
	for stack in allStacks:
		stack.deselect()

def select(selection): # TODO: implement multiple selection
	global originStack
	if isinstance(selection, Card):
		dest = selection.parent
		if originStack:
			moveSelection(dest)
		else:
			originStack = selection.parent
			originStack.select(originStack[originStack.index(selection):])
	elif isinstance(selection, Stack):
		if originStack:
			moveSelection(selection)
		elif selection == stock:
			waste.flip()
			stock.cards = waste.cards
			waste.dump()
		else:
			deselect()
	else:
		deselect()

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
		stock.append(c)

	gameState = State('play')
	startTime = time.time()
	moves = 0
	score = 0

#	testing
# for s in playStacks:
# 	print(s)

#	author: Narbeh Malekian
