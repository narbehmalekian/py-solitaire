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

	def add(stack, *moreCards):
		for card in moreCards:
			if isinstance(card, Cards):
				stack.cards += [card]
			elif isinstance(card, Stack):
				stack.cards += Stack.cards

	def getInfo(stack):
		return 'Stack of:\n'+'\n'.join([card.getInfo() for card in stack.cards])

s = Stack(Card(4,"s"), Card(1,"c"))
print(s.getInfo())
