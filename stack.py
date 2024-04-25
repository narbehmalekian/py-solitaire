from card import *
from typing import *
import math, random

#	helper func for setting position and rotation of the stack
#	converts transform values into tuples
#	num: the number or tuple to be processed into a tuple of numbers
def num2tuple(num):
	if isinstance(num, (int, float)):
		tup = (num,)
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
#	x_pos, y_pos: position of the stack in the window
#		use a tuple to define custom stack shape
#		4 or (4,0) ->	cards at 4, 4, 4, 4 ...
#		(3, 2) -> 		cards at 3, 5, 7, 9 ...
#						   as in 3 +2 +2 +2 ...
#		(0, 1, 1) ->	cards at 0, 1, 3, 7 ...
#						   as in 0 +1 +2 +3 ...
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
		ruleFunc: Callable = lambda a, b: True,
		newDeck: bool = False
	):
		stack.x = num2tuple(x_pos)
		stack.y = num2tuple(y_pos)
		stack.r = num2tuple(rot)
		if newDeck:
			stack.cards = [Card(v, s) for s in Suit for v in Value]
			stack.cards.reverse()
		else:
			stack.cards = [card for group in cards for card in (group if isinstance(group, list) else [group]) if isinstance(card, Card)]
		if tidy:
			stack.tidy()
		stack.rule = ruleFunc

	def shuffle(stack):
		random.shuffle(stack.cards)

	def flip(stack):
		stack.cards.reverse()
		for card in stack.cards:
			card.flip()

	def move(stack, right:float=0, down:float=0, absolute:bool=False, tidy:bool=True):
		stack.x = (right if absolute else right+stack.x[0],) + stack.x[1:]
		stack.y = (down if absolute else down+stack.y[0],) + stack.y[1:]
		if tidy:
			stack.tidy()

	def dump(stack):
		stack.cards = []

	#	positions cards according to the stack's arrangement
	def tidy(stack):
		for cardIndex in range(len(stack.cards)):
			for i, tup in enumerate([stack.x, stack.y, stack.r]):
				result = 0
				#	transformation components are stored in the x, y, and r tuples
				#	(x_pos, Δx_pos, Δ²x_pos, ...)
				for comp in range(len(tup)):
					result += math.comb(cardIndex, comp) * tup[comp]
				c = stack.cards[cardIndex]
				c.pos = c.pos[:i] + (result,) + c.pos[i+1:]

	#	list-like methods for stack using the list stack.cards
	def pop(stack)->Card:
		return stack.cards.pop()
	def __getitem__(stack, i:int)->Card:
		return stack.cards[i]
	def __len__(stack):
		return len(stack.cards)
	#	use append to forcibly add a card to the stack
	def append(stack, moreCards):
		stack.cards.append(moreCards)
	# use stack + card to add a card to the stack only if the card follows the ruleFunc
	def __add__(stack, *moreCards, tidy=True):
		for item in moreCards:

			# add card to stack
			if isinstance(item, Card):
				if stack.rule(stack, item):
					stack.cards += [item]
			elif isinstance(item, Stack):
				stack.cards += item.cards

			# add list of cards to stack
			elif isinstance(item, list):
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

	def __str__(stack):
		return f'Stack of {len(stack.cards)}:\n'+'\n'.join([str(card) for card in stack.cards])+'\n'

	#	does not represent ruleFunc
	def __repr__(stack):
		return f'Stack({stack.cards}, x_pos={stack.x}, y_pos={stack.y}, rot={stack.r}) # ruleFunc not included\n'

#	testing
# s = Stack(Card(4,"s"), Card(1,"c"))
# s += Card(1,'s')
# s += Stack(Card(2,'s'),Card(3,'s'))
# print(repr(s))

# t = Stack(Card(7,'dia'), x_pos=3, y_pos=(2,1))
# print(t.x)

# homerule = lambda s, c : (s.cards[-1].suit == c.suit) & (s.cards[-1].value + 1 == c.value)
# newStack = Stack(Card("a", "s",faceUp=True), ruleFunc = homerule)
# print(newStack)
# newStack + Card(2,"s",faceUp=True)
# print(newStack)
# newStack + Card(3,"c",faceUp=True)
# newStack + Card(4,"d",faceUp=True)
# newStack + Card(4,"s",faceUp=True)
# print(newStack)


#	author: Narbeh Malekian
