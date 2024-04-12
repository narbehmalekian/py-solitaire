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
homestacks = [h1, h2, h3, h4]

p1 = Stack(ruleFunc = playrule)
p2 = Stack(ruleFunc = playrule)
p3 = Stack(ruleFunc = playrule)
p4 = Stack(ruleFunc = playrule)
p5 = Stack(ruleFunc = playrule)
p6 = Stack(ruleFunc = playrule)
p7 = Stack(ruleFunc = playrule)
playstacks = [p1, p2, p3, p4, p5, p6, p7]

h1 = Stack(ruleFunc = handrule)
h2 = Stack(ruleFunc = handrule)

deck = Stack(x_pos = (0,1,-0.04), y_pos = (0,0.1), newDeck = True)


#	testing
# for c in deck.cards:
# 	print(c.pos)
