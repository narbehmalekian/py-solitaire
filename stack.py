from card import *

#
#	Stack Object
#	x_offset: horizontal offset of consecutive cards on the stack
#	y_offset: vertical offset ...
#	cards: cards to be stacked
#
class Stack:
	def __init__(stack, *cards, x_offset=0, y_offset=0):
		stack.x = x_offset
		stack.y = y_offset
		stack.cards = [card for card in cards if isinstance(card, Card)]

	def shuffle(stack):
		stack.cards.shuffle()

	def flip(stack):
		stack.cards.reverse()

	def __add__(stack, *moreCards):
		for card_or_stack in moreCards:
			if isinstance(card_or_stack, Card):
				stack.cards += [card_or_stack]
			elif isinstance(card_or_stack, Stack):
				stack.cards += card_or_stack.cards
			else:
				raise TypeError(f'Object added to a Stack must be of type Stack or Card, not {type(card)}')
		return stack

	#	Removes and returns the top N cards from the stack
	#	n: the number of cards to remove. negative n takes from the bottom
	#	peek: return the card values but leave them in the stack
	def __sub__(stack, n, peek=False):
		# get top n cards
		return

	def __repr__(stack):
		return 'Stack of:\n'+'\n'.join([card.getInfo() for card in stack.cards])

s = Stack(Card(4,"s"), Card(1,"c"))
print(s)
s += Card(1,'s')
s += Stack(Card(2,'s'),Card(3,'s'))
print(s)


#	author: Narbeh Malekian
