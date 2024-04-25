import tkinter as tk
from gameFuncs import *
# from PIL import Image, ImageTk

#
#   layout.py is now gameFuncs.py
#   global varable have been moved to globals.py
#   the other files are imported through the gameFuncs file
#   Use the startGame() function to reset variables, start the game timer, and set the game state
#
startGame()

# function to select a card from button
def selectCard(card):
	print(card)

def renderCard(card, location):
    if card.face: # if card is faceUp, then render it
        rendered_card = tk.Button(location, text=card.name, height=3, width=4, relief="groove", command=lambda: selectCard(card))
    else: # else render it as a Frame (TODO: make back of card nicer)
        rendered_card = tk.Frame(location, borderwidth=2, width=card.w, height=card.h, relief="groove")
        card_label = tk.Label(rendered_card, text='', justify="center", wraplength=40, height=3, width=4, bg="blue")
        card_label.pack()
    rendered_card.place(x=card.x, y=card.y)

def renderStack(stack, stack_location):
    for card in stack:
        renderCard(card, stack_location)

# Create the tkinter window
window = tk.Tk()
window.geometry('700x400')
window.title("Python Solitaire")

# Create the board (contains the rest of the game)
board = tk.Frame(window, width=700, height=400)
board_width = board.winfo_reqwidth()
board_height = board.winfo_reqheight()

# Create the top-left-side of the board (contains the stock and waste stacks)
stock_label = tk.Label(board, text="Stockpile")
stock_label.place(x=board_width*0.1, y=board_height*0.1)
stock.x = (board_width*0.1, 0)
stock.y = (board_height*0.15, 0)
stock.tidy()
renderStack(stock, board)

waste_label = tk.Label(board, text="Waste Pile")
waste_label.place(x=board_width*0.2, y=board_height*0.1)
waste.x = (board_width*0.2, 0)
waste.y = (board_height*0.15, 0)
waste.tidy()
renderStack(waste, board)

# Create the right-side of the board (contains the foundation stacks)
foundation_label = tk.Label(board, text="Foundation Piles")
foundation_label.place(x=board_width*0.6, y=board_height*0.1)

foundation_spacing = 0
for stack in homeStacks:
    stack.x = (board_width*0.6 + foundation_spacing, 0)
    stack.y = (board_height*0.15, 10)
    stack.tidy()
    foundation_spacing = foundation_spacing + board_width*0.1
    renderStack(stack, board)

# Create the center/bottom-side of the board (tablaeu)
tableau_label = tk.Label(board, text="Tableau")
tableau_label.place(x=board_width*0.5, y=board_height*0.4)

talbeau_spacing = 0
for stack in playStacks:
    stack.x = (board_width*0.2 + talbeau_spacing, 0)
    stack.y = (board_height*0.5, 10)
    stack.tidy()
    talbeau_spacing = talbeau_spacing + board_width*0.1
    renderStack(stack, board)


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

# helper function for finding absolute position in board
def on_key_press(event):
    if event.keysym == 'e':
        x = event.x - board.winfo_x()
        y = event.y - board.winfo_y()
        print(f"Mouse Coordinates (relative to board): x={x}, y={y}")
window.bind('<Key>', on_key_press)

# main loop
board.place(x=0,y=0)
window.mainloop()
