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

stock = Stack(ruleFunc = handrule)
waste = Stack(ruleFunc = handrule)

#	generate new deck, shuffle, and deal
deck = Stack(newDeck = True)
deck.shuffle()
#	for playstack number n, deal n cards. Flip the topmost card faceup
for i in range(len(playstacks)):
	for j in range(i+1):
		playstacks[i].append(deck.pop())
	playstacks[i].move(i*playstacks[i][0].width)
	playstacks[i].tidy()
	playstacks[i][-1].flip()
for c in deck:
	stock.append(deck.pop())

#	testing
# for s in playstacks:
# 	print(s)

#	author: Narbeh Malekian
