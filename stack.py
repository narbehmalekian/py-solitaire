from card import *
from typing import *

#	helper func for setting position and rotation of the stack
#	converts transform values into tuples
#	num: the number or tuple to be processed into a tuple of numbers
#	offset: the second element in the tuple
def num2tuple(num, offset=0):
	if isinstance(num, (int, float)):
		tup = (num, offset)
	elif isinstance(num, tuple):
		for n in num:
			if not isinstance(n, (int,float)):
				raise TypeError('Stack position and rotation must be a numbers or tuples of numbers. Got ', num)
		tup = num
	else:
		raise TypeError('Stack position and rotation must be a numbers or tuples of numbers. Got ', num)
	return tup

newDeck = [Card(v, s) for s in Suit for v in Value]
newDeck.reverse()

#
#	Stack Object
#	cards: cards to be stacked (Card objects, or list of Card objects)
#	x/y_pos: position of the stack in the window
#		use a tuple to define custom stack shape
#	rot: rotation of the stack in the window
#		use a tuple to define custom stack shape
#
class Stack:
	def __init__(
		stack,
		*cards,
		x_pos = 0,
		y_pos = 0,
		rot = 0,
		tidy: bool = True,
		ruleFunc: Callable = lambda a, b: True
	):
		if not cards:
			cards = newDeck
		stack.x = num2tuple(x_pos, 0.1)
		stack.y = num2tuple(y_pos)
		stack.r = num2tuple(rot)
		stack.x_transform = []
		stack.y_transform = []
		stack.rot_transform = []
		stack.updateTransforms()
		stack.cards = [card for group in cards for card in (group if isinstance(group, list) else [group]) if isinstance(card, Card)]
		if tidy:
			stack.tidy()
		stack.rule = ruleFunc

	def updateTransforms(stack):
		# for x in range(stack.x):
		# 	stack.x_transform[len(stack.x)-x] =
		return

	def shuffle(stack):
		stack.cards.shuffle()

	def flip(stack):
		stack.cards.reverse()
		for card in stack.cards:
			card.flip()

	#	positions cards according to the stack's arrangement
	def tidy(stack):
		# todo
		pass

	def draw(stack):
		# for card in stack.cards:
		# todo
		pass

	def __getItem__(stack, i:int)->Card:
		return stack.cards[i]

	def __len__(stack):
		return len(stack.cards)

	# tidy is not implemented
	def __add__(stack, *moreCards, tidy=True):
		for item in moreCards:

			# add card to stack
			if isinstance(item, Card):
				if stack.rule(stack, item):
					stack.cards += [item]
			elif isinstance(item, Stack):
				stack.cards += item.cards

			# add list of cards to stack
			elif isinstace(item, list):
				followsRule = True
				for i in range(item-1):
					stack.ruleFunc(item[i+1], Stack(item[i]))
				for card in item:
					if isinstance(card, Card):
						stack.cards += item
			else:
				raise TypeError(f'Object added to a Stack must be of type Stack or Card, not {type(card)}')
		if tidy:
			stack.tidy()
		return stack

	#	Removes and returns the last N cards from the stack
	#	n: the number of cards to remove. negative n takes from the front
	#	peek: return the card values but leave them in the stack
	def __sub__(stack, n, peek=False):
		cards = stack.cards[len(stack)-n:]
		if not peek:
			stack.cards = stack.cards[:len(stack)-n]
		return Stack(cards)

	def __repr__(stack):
		return 'Stack of:\n'+'\n'.join([card.__repr__() for card in stack.cards])+'\n'


#	testing
s = Stack(Card(4,"s"), Card(1,"c"))
s += Card(1,'s')
s += Stack(Card(2,'s'),Card(3,'s'))
t = Stack(Card(7,'dia'), x_pos=3, y_pos=(2,1))
print(t.x)

homerule = lambda s, c : (s.cards[-1].suit == c.suit) & (s.cards[-1].value + 1 == c.value)
newStack = Stack(Card("a", "s",faceUp=True), ruleFunc = homerule)
print(newStack)
newStack + Card(2,"s",faceUp=True)
print(newStack)
newStack + Card(3,"c",faceUp=True)
newStack + Card(4,"d",faceUp=True)
newStack + Card(4,"s",faceUp=True)
print(newStack)

#	author: Narbeh Malekian
