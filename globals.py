from stack import *

#	define a set of rules for the stack layout in a game
homerule = lambda s, c : s[-1].suit == c.suit & s[-1].value + 1 == c.value if s.cards else c.value == 1
playrule = lambda s, c : s[-1].color != c.color & s[-1].value - 1 == c.value
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

selectedCard = None
selectedStack = None

moves = 0
startTime = 0
endTime = 0

#	point values for actions in the game
points = {
	'move': -3,			#	making a card move
	'home': 20,			#	moving a card into it's home stack
	'hand': -1,			#	cycling one card from the stock to the waste
	'per_second': -1	#	spending one second of time playing
}

score = 0
