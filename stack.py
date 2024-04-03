from card import *
from typing import Callable

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

#
#	Stack Object
#	cards: cards to be stacked (Card objects, or list of Card objects)
#	x/y_pos: position of the stack in the window
#		use a tuple to define custom stack shape
#	rot: rotation of the stack in the window
#		use a tuple to define custom stack shape
#
class Stack:
	def __init__(stack, *cards: [Card, List[Card]], x_pos=0, y_pos=0, rot=0, tidy=True: Boolean, ruleFunc=(lambda a b:return True): Callable):
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
	def tidy():
		# todo
		return

	def draw(stack):
		# for card in stack.cards:
		# todo
		return

	def __len__(stack):
		return len(stack.cards)

	# tidy is not implemented
	def __add__(stack, *moreCards, tidy=True):
		for item in moreCards:
			if isinstance(item, Card):
				if stack.rule(stack, item):
					stack.cards += [item]
			elif isinstance(item, Stack):
				stack.cards += item.cards
			elif isinstace(item, list):
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

#	author: Narbeh Malekian
