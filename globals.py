from stack import *

#
#	THEMING
#

headerColor = '#102'
bgColor = '#213'
cardColor = '#68F'
textColor = '#DDF'

#
#	GAME STATE
#

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

# selectedCard = None
originStack = None

#
#	GAME BOARD
#

#	define the rules for moving cards to each type of stack in solitaire
homerule = lambda s, c : ((s[-1].suit == c.suit) & (s[-1].value + 1 == c.value)) if s.cards else c.value == 1
	# if s.cards:
	# 	return (s[-1].suit == c.suit) & (s[-1].value + 1 == c.value)
	# else:
	# 	return c.value == 1
playrule = lambda s, c : ((s[-1].color != c.color) & (s[-1].value - 1 == c.value)) if s.cards else c.value == 13
handrule = lambda s, c : False
emptyrule = lambda s, c : c.value == 13

#	define the stacks in play
h1 = Stack(ruleFunc = homerule)
h2 = Stack(ruleFunc = homerule)
h3 = Stack(ruleFunc = homerule)
h4 = Stack(ruleFunc = homerule)
homeStacks = [h1, h2, h3, h4]

p1 = Stack(ruleFunc = playrule)
p2 = Stack(ruleFunc = playrule)
p3 = Stack(ruleFunc = playrule)
p4 = Stack(ruleFunc = playrule)
p5 = Stack(ruleFunc = playrule)
p6 = Stack(ruleFunc = playrule)
p7 = Stack(ruleFunc = playrule)
playStacks = [p1, p2, p3, p4, p5, p6, p7]

stock = Stack(ruleFunc = handrule)
waste = Stack(ruleFunc = handrule)

allStacks = [s for l in [playStacks, homeStacks, [stock, waste]] for s in l]

#
#	GAME SCORING
#

startTime = 0
endTime = 0
moves = 0
score = 0

#	point value assignments for actions in the game
points = {
	'move': -3,			#	making a card move
	'home': 20,			#	moving a card into it's home stack
	'hand': -1,			#	cycling one card from the stock to the waste
	'per_second': -1	#	spending one second of time playing
}

#	author: Narbeh Malekian
