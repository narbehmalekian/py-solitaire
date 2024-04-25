from globals import *
import time

#	TODO: implement multiple selection
def select(selection, multiple=False):
	if isinstance(selection, Card):
		selectedCard = selection
	elif isinstance(selection, Stack):
		selectedStack = selection
	else:
		selectedCard = None

class State(StrEnum):
	START = 'start'
	PLAY = 'play'
	WON = 'won'
	# check first letter of string to infer intended gamestate
	@classmethod
	def _missing_(cls, value):
		return{
			's': cls.START,
			'p': cls.PLAY,
			'w': cls.WON
		}.get(value.lower()[0:1], None)
gameState = State('start')

def checkWon(){
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
}

def gameTime():
	if gameState = State('start'):
		return 0
	if gameState = State('play'):
		return time.time() - startTime
	if gameState = State('won'):
		return endTime - startTime

def startGame():
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

#	testing
# for s in playstacks:
# 	print(s)

#	author: Narbeh Malekian
