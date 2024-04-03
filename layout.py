from stack import *

#	define a set of rules for the stack layout in a game
homestackrule = lambda s, c : s[-1].suit == c.suit & s[-1].value + 1 == c.value
playstackrule = lambda s, c : s[-1].color != c.color & s[-1].value - 1 == c.value
handstackrule = lambda s, c : False
emptystackrule = lambda s, c : c.value == 13
