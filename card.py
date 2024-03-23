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
	def __init__(card, v, s, f=False):
		card._value = Value(v)
		card._suit = Suit(s)
		card.face = f

	@property
	def color(card):
		return Color.BLACK if card.suit in [Suit.SPADE, Suit.CLUB] else Color.RED

	@property
	def value(card):
		return card._value

	@property
	def suit(card):
		return card._suit

	def flip(card):
		card.face = not card.face

	def __repr__(card):
		return f'{card.value.name} of {card.suit.name}S facing {"UP" if card.face else "DOWN"}'


# testing
c = Card(4,'s')
print(c.face)
c.flip()
print(c.face)
print(c)

#	author: Narbeh Malekian
