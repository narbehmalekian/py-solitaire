from enum import Enum, StrEnum, IntEnum

class Suit(StrEnum):
	SPADE = 'spade'
	HEART = 'heart'
	CLUB = 'club'
	DIAMOND = 'diamond'

	# check first letter of string to infer intended suit name
	@classmethod
	def _missing_(cls, value):
		return{
			's': cls.SPADE,
			'h': cls.HEART,
			'c': cls.CLUB,
			'd': cls.DIAMOND
		}.get(value.lower()[0:1], None)
		# dictionary lookup is cleaner than match/case or if/elif/else
		# https://stackoverflow.com/a/103081

class Color(StrEnum):
	BLACK = 'black'
	RED = 'red'

	@classmethod
	def _missing_(cls, value):
		return{
			'b': cls.BLACK,
			'r': cls.RED
		}.get(value.lower()[0:1], None)

class Value(IntEnum):
	ACE = 1
	TWO = 2
	THREE = 3
	FOUR = 4
	FIVE = 5
	SIX = 6
	SEVEN =7
	EIGHT = 8
	NINE = 9
	TEN = 10
	JACK = 11
	QUEEN = 12
	KING = 13

	# supports integer and string value initialization
	@classmethod
	def _missing_(cls, value):
		return {
			'a': cls.ACE,
			'j': cls.JACK,
			'q': cls.QUEEN,
			'k': cls.KING
		}.get(value.lower()[0:1], None)

#
#	Card Object
#	v: value of the card (Value.FOUR, 1..13, 'Ace', 'QUEEN', 'j')
#	s: suit of the card (Suit.SPADE, 'club', 'HEART', 'D')
#	f: is the card face-up (boolean)
#
class Card:
	def __init__(card, value, suit, position=(0,0,0), faceUp=False, height=7, width=5):
		card._val = Value(value)
		card._suit = Suit(suit)
		card.h = height
		card.w = width
		if not isinstance(faceUp, bool):
			raise TypeError('Card faceUp orientation must be boolean. Got: ', faceUp)
		card.face = faceUp 
		if not isinstance(position, tuple) or not len(position) == 3:
			raise TypeError('Card position must be a tuple of length 3, in the form (x, y, rotation). Got: ', position)
		for i in range(3):
			if not isinstance(position[i], (int,float)):
				raise TypeError('Card position values must be numeric, in the form (x, y, rotation). Got: ', position)
		card.pos = position

	@property
	def x(card):
		return card.position[0]

	@property
	def y(card):
		return card.position[1]

	@property
	def rot(card):
		return card.position[2]

	@property
	def color(card):
		return Color.BLACK if card.suit in [Suit.SPADE, Suit.CLUB] else Color.RED

	@property
	def value(card):
		return card._val

	@property
	def suit(card):
		return card._suit

	@property
	def height(card):
		return card.h

	@property
	def width(card):
		return card.w

	def flip(card):
		card.face = not card.face

	def draw(card):
		#	will integrate into GUI
		#	this function may not need to be here
		return

	#	a compact text representation of the card (A♤, Q♥, etc)
	@property
	def name(card):
		values = {1:'A', 2:'2', 3:'3', 4:'4', 5:'5', 6:'6', 7:'7', 8:'8', 9:'9', 10:'10', 11:'J', 12:'Q', 13:'K'}
		suits = {'spade':'♤','heart':'♥','club':'♧','diamond':'♦'}
		return values.get(card.value.value) + suits.get(card.suit.value)

	def __repr__(card):
		# return f'{card.value.name} of {card.suit.name}S facing {"UP" if card.face else "DOWN"}'
		# return f'{card.value.name} of {card.suit.name}S' if card.face else '?'
		return card.name if card.face else '_'


# testing
# c = Card(4,'s')
# print(c.face)
# c.flip()
# print(c.face)
# print(c)

#	author: Narbeh Malekian
