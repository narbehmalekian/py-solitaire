import tkinter as tk
from gameFuncs import *
# from PIL import Image, ImageTk

def click(button):
    if isinstance(button, Card):
        card = button
        if card.face:
            select(card)
        elif card.parent == stock:
            select(card)
            select(waste)
        elif card == card.parent[-1]:
            card.flip()
    elif isinstance(button, Stack):
        stack = button
        if stack == stock:
            select(stack)
        elif stack == waste:
            select(stock[-1])
            select(waste)
        else:
            select(stack)
    refresh()

# render a single card, location is the frame it as attached to
def renderCard(card, location):
    if card.face: # if card is faceUp, then render it as a button
        rendered_card = tk.Button(location, anchor='n', font=('Arial', 16), fg=card.color, text=card.name, command=lambda: click(card))
    else: # else render it as a Frame (TODO: make back of card nicer)
        rendered_card = tk.Button(location, borderwidth=2, width=4, height=3, bg=cardColor, command=lambda: click(card))
        # card_label = tk.Label(rendered_card, text='', justify="center", wraplength=40, height=3, width=4, bg=cardColor, fg=textColor)
        # card_label.pack()
    rendered_card.place(relx=card.x, rely=card.y)

# render a stack of cards
def renderStack(stack, stack_location):
    if len(stack) == 0: # empty stack (no cards)
        empty_stack = tk.Button(stack_location, text="", width=4, height=3, bg=bgColor, command=lambda: click(stack))
        empty_stack.place(relx=stack.x[0], rely=stack.y[0])
    else:
        for card in stack:
            renderCard(card, stack_location)

# render each of the labels in the board
def renderLabels():
    # stock label
    stock_label = tk.Label(board, text="Stockpile", bg=bgColor, fg=textColor)
    stock_label.place(relx=0.09, rely=0.05)
    # waste label
    waste_label = tk.Label(board, text="Waste Pile", bg=bgColor, fg=textColor)
    waste_label.place(relx=0.19, rely=0.05)
    # foundation label
    foundation_label = tk.Label(board, text="Foundation Piles", bg=bgColor, fg=textColor)
    foundation_label.place(relx=0.6, rely=0.05)
    # tableau label
    tableau_label = tk.Label(board, text="Tableau", bg=bgColor, fg=textColor)
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
        stack.x = (0.5 + foundation_spacing, 0)
        stack.y = (0.15, 0.01)
        stack.tidy()
        foundation_spacing = foundation_spacing + 0.1 # <- change this value if needed
        renderStack(stack, board)
    # set the relative position of the tablaeu stacks/play stacks
    talbeau_spacing = 0
    for stack in playStacks:
        stack.x = (0.2 + talbeau_spacing, 0)
        stack.y = (0.5, 0.03)
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

def refresh():
    clearBoard()
    renderLabels()
    renderBoard()

# call once at the start of a game
def initializeNewGame():
    startGame()
    refresh()

# create the tkinter window
window = tk.Tk()
window.geometry("700x400")
window.title("Python Solitaire")
window.configure(bg=headerColor)

# create the game board
global board_width, board_height
board_width = 700
board_height = 600
board = tk.Frame(window, width=board_width, height=board_height, bg=bgColor)

# create the top UI
top_frame = tk.LabelFrame(window, text="Info", height=40, width=600, bg=headerColor, fg=textColor)
timer_label = tk.Label(top_frame, text=("Time: "), bg=headerColor, fg=textColor)
timer_label.grid(row=0, column=0, padx=10)
moves_label = tk.Label(top_frame, text="Moves: ", bg=headerColor, fg=textColor)
moves_label.grid(row=0, column=1, padx=10)
score_label = tk.Label(top_frame, text="Score: ", bg=headerColor, fg=textColor)
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
# while not checkWon():
#     window.update_idletasks()
#     window.update()
