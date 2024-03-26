from card import *
import random, time

clubhome = []
spadehome = []
hearthome = []
diamondhome = []

stack1 = []
stack2 = []
stack3 = []
stack4 = []
stack5 = []
stack6 = []
stack7 = []

hand = []

stacks = [
	clubhome, spadehome, hearthome, diamondhome,
	stack1, stack2, stack3, stack4, stack5, stack6, stack7,
	hand
]

homestacks= [
	spadehome, hearthome, clubhome, diamondhome
]

playstacks = [
	stack1, stack2, stack3, stack4, stack5, stack6, stack7
]

newDeck = [Card(val, suit) for suit in Suit for val in Value]
random.shuffle(newDeck)

for i in range(0,7):
	for j in range(i+1):
		playstacks[i].append(newDeck.pop())
	playstacks[i][i].flip()

# testing
# stack1.append(Card(2,'d'))
# stack1[-1].flip()
# stack2.append(Card(1,"d"))
# stack2[-1].flip()

for card in newDeck:
	hand.append(card)

def fliplast():
	hand[len(hand)-1].flip()

fliplast()

def rotated(l, n):
	return l[n:] + l[:n]

def next():
	if hand:
		fliplast()
		hand.append(hand.pop(0))
		fliplast()
	else:
		print('Hand is empty.')

def showgame():
	print('  Home Stacks')
	for i in range(len(homestacks)):
		print({1:'a ',2:'b ',3:'c ',4:'d '}.get(i+1), end='')
		print(homestacks[i])
	print('\n  Play Stacks')
	for i in range(len(playstacks)):
		print(str(i+1)+' ', end='')
		print(playstacks[i])
	print('\n  Your Hand')
	print('h ', end='')
	print(hand)
	print()

def win():
	for stack in playstacks:
		if stack:
			return False
	if hand:
		return False
	return True

stacklookup = {'a':spadehome, 'b':hearthome, 'c':clubhome, 'd':diamondhome, '1':stack1, '2':stack2, '3':stack3, '4':stack4, '5':stack5, '6':stack6, '7':stack7, 'h':hand}
def validMove(o, d):
	orig = stacklookup.get(o)
	dest = stacklookup.get(d)
	if not orig:
		return False
	if o in 'abcd1234567h' and d in 'abcd1234567':
		
		if d in 'abcd':
			last = orig[-1]

			# home is empty, orig must end with ace
			if len(dest) == 0:
				return last.value == 1

			# home has cards, use home rules
			else:
				return (last.value == 1+dest[-1].value) and (last.suit == dest[-1].suit)
		
		elif d in '1234567':
			if len(dest) == 0:
				for card in orig:
					if card.face and card.value == 13:
						return True
			else:
				for card in orig:
					if card.face and card.value == dest[-1].value-1 and card.color != dest[-1].color:
						return True
	return False

def help():
	print('In solitaire, the goal is to organize all the cards into the Home Stacks.')
	print('Cards must be placed, in order, A, 2, 3, ... 10 , J, Q, K, into stacks of matching suit.')
	print('Most of the cards are hidden in the Play Stacks and in your hand.')
	print('To reveal the cards, you can move them in your Play Stacks, but according to the following rules:')
	print('A card must be placed on another card with value ONE greater than itself.')
	print('A card must be placed on another card of opposite color to itself.')
	print('Except a king, which must be placed in an empty stack.')
	print()
	print('Next to each stack is an identifying number or letter.')
	print('Use these identifiers to select an origin and destination stack.')
	print('The game will move the card or cards to the stack you select.')
	print('Example: to move a card from Play Stack \'4\' to Home Stack \'a\', type 4a')
	print('There are also 2 shortcuts:')
	print('Type just the stack number to send your hand card to that stack number.')
	print('Type just the home letter to send the next card of the matching suit to that home stack.')
	print()
	print('Here are some other commands:')
	print('Enter - show the next card in your hand')
	print('quit - ends the game')
	print('help - shows this message')
	print()
	print('Have fun playing!\n')
	input('Press Enter to return to the game.\n')

def play():
	input('Welcome to solitaire!\nType help at any time after starting the game to learn how to play.\n\nPress Enter to begin!\n')
	ctmoves = 0
	t = time.time()
	while not win():
		showgame()
		move = input('> ')
		if len(move) == 1:
			# hand to stack shortcut
			if move in '1234567':
				move = 'h' + move
			# send home shortcut
			elif move in 'abcd':
				c = '0'
				home = stacklookup.get(move)
				if home:
					v = home[-1].value + 1
					s = home[-1].suit
					for i in range(len(playstacks)):
						if playstacks[i]:
							if playstacks[i][-1].suit == s and playstacks[i][-1].value == v:
								c = str(i+1)
					# send home from hand
					if hand:
						if hand[-1].suit == s and hand[-1].value == v:
							c = 'h'
				# else:
				# 	#move an ace
				move = c + move
		if move == '':
			ctmoves += 1
			next()
		elif move == 'quit':
			exit()
		elif move == 'help':
			help()
		elif len(move) >= 2:
			o = move[0]
			d = move[1]
			if validMove(o, d):
				ctmoves += 1
				orig = stacklookup.get(o)
				dest = stacklookup.get(d)
				if d in 'abcd':
					dest.append(orig.pop())
				else:
					destCval = 14
					destCcol = None
					if dest:
						destCval = dest[-1].value
						destCcol = dest[-1].color
					temp = [orig.pop()]
					print(f'temp moving list: {temp}')
					while temp[-1].value != destCval-1 or temp[-1].color == destCcol:
						temp.append(orig.pop())
						print(temp)
					temp.reverse()
					for c in temp:
						dest.append(c)
				if orig:
					orig[-1].face = True
			elif move == 'force win':
				for stack in playstacks:
					while stack:
						stack.pop()
				while hand:
					hand.pop()
			else:
				print('That\'s not a valid move!\n')
		else:
			print('That command is not recognized. Please try again.\nFor possible commands, type help\n')
	print(f'You won with {ctmoves} moves in {int((time.time()-t)//60)} min {int((time.time()-t)%60)} sec!')

play()
