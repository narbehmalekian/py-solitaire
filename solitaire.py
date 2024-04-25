import tkinter as tk
from card import *
from stack import *
from layout import *
# from PIL import Image, ImageTk

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


# # Create the top frame (contains UI such as moves, time, etc.)
# top_frame = tk.LabelFrame(window, text="Info", height=40, width=400)

# timer_label = tk.Label(top_frame, text="Time: ")
# timer_label.grid(row=0, column=0, padx=10)

# moves_label = tk.Label(top_frame, text="Moves: ")
# moves_label.grid(row=0, column=1, padx=10)

# score_label = tk.Label(top_frame, text="Score: ")
# score_label.grid(row=0, column=2, padx=10)

# top_frame.pack()

# Create the board (contains the rest of the game)
board = tk.Frame(window, width=700, height=400)
# print(str(board.winfo_reqwidth()) + "x" + str(board.winfo_reqheight()))

# Create the top-left-side of the board (contains the stock and waste stacks)
stock_label = tk.Label(board, text="Stockpile")
stock_label.place(x=board.winfo_reqwidth()*0.1, y=board.winfo_reqheight()*0.1)
stock.x = (board.winfo_reqwidth()*0.1, 0)
stock.y = (board.winfo_reqheight()*0.15, 0)
stock.tidy()
renderStack(stock, board)

waste_label = tk.Label(board, text="Waste Pile")
waste_label.place(x=board.winfo_reqwidth()*0.2, y=board.winfo_reqheight()*0.1)
waste.x = (board.winfo_reqwidth()*0.2, 0)
waste.y = (board.winfo_reqheight()*0.15, 0)
waste.tidy()
renderStack(waste, board)

# Create the right-side of the board (contains the foundation stacks)
foundation_label = tk.Label(board, text="Foundation Piles")
foundation_label.place(x=board.winfo_reqwidth()*0.6, y=board.winfo_reqheight()*0.1)

foundation_spacing = 0
for stack in homestacks:
    stack.x = (board.winfo_reqwidth()*0.6 + foundation_spacing, 0)
    stack.y = (board.winfo_reqheight()*0.15, 10)
    stack.tidy()
    foundation_spacing = foundation_spacing + board.winfo_reqwidth()*0.1
    renderStack(stack, board)

# Create the center/bottom-side of the board (tablaeu)
tableau_label = tk.Label(board, text="Tableau")
tableau_label.place(x=board.winfo_reqwidth()*0.5, y=board.winfo_reqheight()*0.4)

talbeau_spacing = 0
for stack in playstacks:
    stack.x = (board.winfo_reqwidth()*0.2 + talbeau_spacing, 0)
    stack.y = (board.winfo_reqheight()*0.5, 10)
    stack.tidy()
    talbeau_spacing = talbeau_spacing + board.winfo_reqwidth()*0.1
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

# TODO: 
#   * add padding to each of the frames where necessary
#   * make the timer work
#   * use variables for each of the pile sizes (length and width) instead of hardcoding, also lets you change them elsewhere
