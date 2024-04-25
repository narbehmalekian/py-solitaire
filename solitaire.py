import tkinter as tk
from card import *
from stack import *
import random, time
# from PIL import Image, ImageTk

def selectCard(card):
	print(card)

def renderCard(card, location, card_x, card_y):
    if card.face: # if card is faceUp, then render it (maybe as a button)
        rendered_card = tk.Button(location, text=card.name, width=4, height=3, relief="groove", command=lambda: selectCard(card))
    else: # else render it as a Frame (TODO: make back of card nicer)
        rendered_card = tk.Frame(location, borderwidth=2, width=card.w, height=card.h, relief="groove")
        card_label = tk.Label(rendered_card, text='', justify="center", wraplength=40, height=3, width=4, bg="blue")
        card_label.pack()
    rendered_card.place(x=card_x, y=card_y)

# distance is the space between cards in a stack, maybe change variable name for clarity
def renderStack(stack, location, stack_x, stack_y, distance):
    new_y = stack_y
    for card in stack:
        renderCard(card, location, stack_x, new_y)
        new_y = new_y + distance

# Create the tkinter window
window = tk.Tk()
window.geometry('700x400')
window.title("Python Solitaire")


# Create the top frame (contains UI such as moves, time, etc.)
top_frame = tk.LabelFrame(window, text="Info", height=40, width=600)

timer_label = tk.Label(top_frame, text="Time: ")
timer_label.grid(row=0, column=0, padx=10)

moves_label = tk.Label(top_frame, text="Moves: ")
moves_label.grid(row=0, column=1, padx=10)

score_label = tk.Label(top_frame, text="Score: ")
score_label.grid(row=0, column=2, padx=10)

top_frame.pack()


# Create the left-side frame (contains the stock and waste stacks)
left_frame = tk.Frame(window, width=60, padx=5)

stock_pile = tk.LabelFrame(left_frame, text="Stock", padx=5, pady=5, width=55, height=80, borderwidth=2, relief="sunken")
stock_pile.pack()

waste_pile = tk.LabelFrame(left_frame, text="Waste", padx=5, pady=5, width=55, height=80, borderwidth=2, relief="sunken")
waste_pile.pack()

left_frame.pack( side = "left")


# Create the right-side frame (contains the foundation stacks)
right_frame = tk.Frame(window, width=60, height=260, padx=5)

# Create an array to hold the foundation piles
foundation_piles = []

# Create and store foundation piles in the array
for i in range(1, 5):
    foundation_pile = tk.LabelFrame(right_frame, text=f"Pile {i}", padx=5, pady=5, width=55, height=80, borderwidth=2, relief="sunken")
    foundation_pile.grid(row=i-1, column=0, pady=5)
    foundation_piles.append(foundation_pile)

right_frame.pack(side="right")

# Create the center/bottom-side frame (tablaeu)
tablaeu = tk.Frame(window, height=250, width=500)

i = 0
tablaeu_piles = []
for i in range(1, 8):
    pile = tk.LabelFrame(tablaeu, text=str(i), padx=5, width=55, height=250)
    pile.grid(row=0, column=i, padx=10)
    tablaeu_piles.append(pile)

tablaeu.pack( side = "top")

# Create the menu and functions
def donothing():
   x = 0
 
menubar = tk.Menu(window)
filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label="New Game", command=donothing)
filemenu.add_command(label="Undo", command=donothing)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=window.quit)
menubar.add_cascade(label="Game", menu=filemenu)

helpmenu = tk.Menu(menubar, tearoff=0)
helpmenu.add_command(label="How to Play", command=donothing)
helpmenu.add_command(label="About...", command=donothing)
menubar.add_cascade(label="Help", menu=helpmenu)

window.config(menu=menubar)

# setup and start/show game
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
	# Home Stacks
	for i in range(len(homestacks)):
		renderStack(homestacks[i], foundation_piles[i], 0, 0, 10)
	# Play Stacks
	for i in range(len(playstacks)):
		renderStack(playstacks[i], tablaeu_piles[i], 0, 0, 5)

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

# def play():
# 	ctmoves = 0
# 	t = time.time()
# 	while not win():
# 		t = time.time()
# 		showgame()
# 		move = input('> ')
# 		if len(move) == 1:
# 			# hand to stack shortcut
# 			if move in '1234567':
# 				move = 'h' + move
# 			# send home shortcut
# 			elif move in 'abcd':
# 				c = '0'
# 				home = stacklookup.get(move)
# 				if home:
# 					v = home[-1].value + 1
# 					s = home[-1].suit
# 					for i in range(len(playstacks)):
# 						if playstacks[i]:
# 							if playstacks[i][-1].suit == s and playstacks[i][-1].value == v:
# 								c = str(i+1)
# 					# send home from hand
# 					if hand:
# 						if hand[-1].suit == s and hand[-1].value == v:
# 							c = 'h'
# 				# else:
# 				# 	#move an ace
# 				move = c + move
# 		if move == '':
# 			ctmoves += 1
# 			next()
# 		elif move == 'quit':
# 			exit()
# 		elif move == 'help':
# 			help()
# 		elif len(move) >= 2:
# 			o = move[0]
# 			d = move[1]
# 			if validMove(o, d):
# 				ctmoves += 1
# 				orig = stacklookup.get(o)
# 				dest = stacklookup.get(d)
# 				if d in 'abcd':
# 					dest.append(orig.pop())
# 				else:
# 					destCval = 14
# 					destCcol = None
# 					if dest:
# 						destCval = dest[-1].value
# 						destCcol = dest[-1].color
# 					temp = [orig.pop()]
# 					while temp[-1].value != destCval-1 or temp[-1].color == destCcol:
# 						temp.append(orig.pop())
# 					temp.reverse()
# 					for c in temp:
# 						dest.append(c)
# 				if orig:
# 					orig[-1].face = True
# 			elif move == 'force win':
# 				for stack in playstacks:
# 					while stack:
# 						stack.pop()
# 				while hand:
# 					hand.pop()
# 			else:
# 				print('That\'s not a valid move!\n')
# 		else:
# 			print('That command is not recognized. Please try again.\nFor possible commands, type help\n')
# 	showgame()
# 	c = True if ((time.time()-t)//60<1) else False # check if user cheated
# 	q = '\"' # double quote string bc fstring complains about the backslash
# 	print(f'You {"cheated and "+q if c else ""}won{q if c else ""} with {ctmoves} moves in {int((time.time()-t)//60)} min, {int((time.time()-t)%60)} sec!\n')
# 	input("Press Enter to exit")

temp_button = tk.Button(window, text="Temp", padx=10, pady=10, command=showgame)
temp_button.pack( side = "bottom")

# main loop
window.mainloop()

# TODO: 
#   * add padding to each of the frames where necessary
#   * make the timer work
#   * use variables for each of the pile sizes (length and width) instead of hardcoding, also lets you change them elsewhere
