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
		stack.cards = [card for group in cards for card in (group if isinstance(group, list) else [group]) if isinstance(card, Card)]

	def shuffle(stack):
		stack.cards.shuffle()

	def flip(stack):
		stack.cards.reverse()
		for card in stack.cards:
			card.flip()

	def __len__(stack):
		return len(stack.cards)

	def __add__(stack, *moreCards):
		for item in moreCards:
			if isinstance(item, Card):
				stack.cards += [item]
			elif isinstance(item, Stack):
				stack.cards += item.cards
			elif isinstace(item, list):
				for card in item:
					if isinstance(card, Card):
						stack.cards += item
			else:
				raise TypeError(f'Object added to a Stack must be of type Stack or Card, not {type(card)}')
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
		return 'Stack of:\n'+'\n'.join([card.__repr__() for card in stack.cards])


#	testing
s = Stack(Card(4,"s"), Card(1,"c"))
print(s)
s += Card(1,'s')
s += Stack(Card(2,'s'),Card(3,'s'))
print(s)
c = s - 1
print(s)
print(c)

#	author: Narbeh Malekian
