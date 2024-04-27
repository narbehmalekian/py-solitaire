import tkinter as tk
from gameFuncs import *
# from PIL import Image, ImageTk

# render a single card, location is the frame it as attached to
def renderCard(card, location):
    if card.face: # if card is faceUp, then render it as a button
        rendered_card = tk.Button(location, text=card.name, width=4, height=3, relief="groove", command=lambda: select(card))
    else: # else render it as a Frame (TODO: make back of card nicer)
        rendered_card = tk.Frame(location, borderwidth=2, width=card.w, height=card.h, relief="groove")
        card_label = tk.Label(rendered_card, text='', justify="center", wraplength=40, height=3, width=4, bg="blue")
        card_label.pack()
    rendered_card.place(relx=card.x, rely=card.y)

# render a stack of cards
def renderStack(stack, stack_location):
    if stack.__len__ == 1:
        print("empty stack")
    for card in stack:
        renderCard(card, stack_location)

# render each of the labels in the board
def renderLabels():
    # stock label
    stock_label = tk.Label(board, text="Stockpile", bg="green")
    stock_label.place(relx=0.1, rely=0.1)
    # waste label
    waste_label = tk.Label(board, text="Waste Pile", bg="green")
    waste_label.place(relx=0.2, rely=0.1)
    # foundation label
    foundation_label = tk.Label(board, text="Foundation Piles", bg="green")
    foundation_label.place(relx=0.6, rely=0.1)
    # tableau label
    tableau_label = tk.Label(board, text="Tableau", bg="green")
    tableau_label.place(relx=0.5, rely=0.4)

# set the position of every stack, then render all of them
def renderBoard():
    # set the relative position of the stock and waste stacks
    stock.x = (0.1, 0)
    stock.y = (0.15, 0)
    waste.x = (0.2, 0)
    waste.y = (0.15, 0)
    # set the relative position of the foundation stacks/home stacks
    foundation_spacing = 0
    for stack in homeStacks:
        stack.x = (0.6 + foundation_spacing, 0)
        stack.y = (0.15, 0.01)
        stack.tidy()
        foundation_spacing = foundation_spacing + 0.1 # <- change this value if needed
        renderStack(stack, board)
    # set the relative position of the tablaeu stacks/play stacks
    talbeau_spacing = 0
    for stack in playStacks:
        stack.x = (0.2 + talbeau_spacing, 0)
        stack.y = (0.5, 0.025)
        talbeau_spacing = talbeau_spacing + 0.1
    # render all stacks
    for stack in allStacks:
        stack.tidy()
        renderStack(stack, board)

# function to clear all the stacks from the board
def clearBoard():
    # clear the stacks and labels
    for widgets in board.winfo_children():
        widgets.destroy()

# call once at the start of a game
def initializeNewGame():
    startGame()
    clearBoard()
    renderLabels()
    renderBoard()

# create the tkinter window
window = tk.Tk()
window.geometry("700x400")
window.title("Python Solitaire")
window.configure(bg="light goldenrod")

# create the game board
global board_width, board_height
board_width = 700
board_height = 400
board = tk.Frame(window, width=board_width, height=board_height, bg="green")

# create the top UI
top_frame = tk.LabelFrame(window, text="Info", height=40, width=600, bg="light goldenrod")
timer_label = tk.Label(top_frame, text=("Time: "), bg="light goldenrod")
timer_label.grid(row=0, column=0, padx=10)
moves_label = tk.Label(top_frame, text="Moves: ", bg="light goldenrod")
moves_label.grid(row=0, column=1, padx=10)
score_label = tk.Label(top_frame, text="Score: ", bg="light goldenrod")
score_label.grid(row=0, column=2, padx=10)
top_frame.pack()

# Create the menu and functions
def donothing():
   x = 0
 
menubar = tk.Menu(window)
filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label="New Game", command=initializeNewGame)
filemenu.add_command(label="Undo", command=donothing)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=window.quit)
menubar.add_cascade(label="Game", menu=filemenu)

helpmenu = tk.Menu(menubar, tearoff=0)
helpmenu.add_command(label="How to Play", command=donothing)
helpmenu.add_command(label="About...", command=donothing)
menubar.add_cascade(label="Help", menu=helpmenu)

window.config(menu=menubar)

# helper function for debugging
def on_key_press(event):
    if event.keysym == 'q': # check absolute position of pointer on board
        x = event.x - board.winfo_x()
        y = event.y - board.winfo_y()
        print(f"Mouse Coordinates (relative to board): x={x}, y={y}")
    elif event.keysym == 'w':
        print(selectedCard)
    elif event.keysym == 'e':
        print(selectedStack)
    elif event.keysym == 'r':
        print(str(board.winfo_width()) + "x" + str(board.winfo_height()))

# bind the functions to window
window.bind('<Key>', on_key_press)

initializeNewGame()
board.pack(side= "left", expand=True, fill="both")
# main loop
window.mainloop()
