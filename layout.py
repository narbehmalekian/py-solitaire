from stack import *

#	define a set of rules for the stack layout in a game
homerule = lambda s, c : s[-1].suit == c.suit & s[-1].value + 1 == c.value
playrule = lambda s, c : s[-1].color != c.color & s[-1].value - 1 == c.value
handrule = lambda s, c : False
emptyrule = lambda s, c : c.value == 13

#	define the stacks in play
h1 = Stack(ruleFunc = emptyrule)
h2 = Stack(ruleFunc = emptyrule)
h3 = Stack(ruleFunc = emptyrule)
h4 = Stack(ruleFunc = emptyrule)
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

