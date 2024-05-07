import tkinter as tk
from gameFuncs import *
# from PIL import Image, ImageTk

selectedCard = None
selectedStack = None
chosen = False # flag, False means card has not been chosen, True means card has been chosen
num_cards = 1

# move num_cards from source to destination
def moveCards(source_stack, destination_stack, num_cards):
    global chosen

    # create a temporary clone of the source stack
    source_clone = Stack(ruleFunc=None)
    source_clone += source_stack

    # create a temporary stack to hold the cards to be moved
    cards_to_move = Stack(ruleFunc=None)

    # pop the specified number of cards from the cloned stack
    for _ in range(num_cards):
        if source_clone:
            cards_to_move.append(source_clone.pop())

    # check if top card can be added to the destination stack according to its rule
    can_move = destination_stack.rule(destination_stack, cards_to_move[-1])

    if can_move:
        # add the cards to the destination stack
        for card in reversed(cards_to_move):
            destination_stack += card

        # remove the cards from the actual source stack
        for _ in range(num_cards):
            source_stack.pop()

        # flip the last card in the source stack if it's face down
        if source_stack and not source_stack[-1].face:
            source_stack[-1].flip()
    else:
        print("Invalid Move")
    chosen = False

    clearBoard()
    renderBoard()

# render a single card, location is the frame it as attached to
def renderWasteCard(card, location):
    if card.face: # if card is faceUp, then render it as a button
        rendered_card = tk.Button(location, text=card.name, width=cardWidth, height=cardHeight, relief="groove", command=lambda: wasteClick(card))
    else: # else render it as a Frame (TODO: make back of card nicer)
        rendered_card = tk.Frame(location, borderwidth=2, width=card.w, height=card.h, relief="groove")
        card_label = tk.Label(rendered_card, text='', justify="center", wraplength=40, height=cardHeight, width=cardWidth, bg=cardColor)
        card_label.pack()
    rendered_card.place(relx=card.x, rely=card.y)

# render a stack of cards, used for waste pile
def renderWasteStack(stack, stack_location): 
    if len(stack) == 0: # empty stack (no cards)
        empty_stack = tk.Button(stack_location, width=cardWidth, height=cardHeight, relief="groove", bg=headerColor) # no command
        empty_stack.place(relx=stack.x[0], rely=stack.y[0])
    else:
        for card in stack:
            renderWasteCard(card, stack_location)

def wasteClick(card):
    global selectedCard, selectedStack, chosen
    if chosen == False:
        selectedCard = card
        selectedStack = waste
        chosen = True
    elif chosen == True:
        print("You cannot move cards into the waste pile")
        chosen = False

# render a play stack
def renderPlayStack(stack, stack_location): 
    if len(stack) == 0: # empty stack (no cards)
        empty_stack = tk.Button(stack_location, width=cardWidth, height=cardHeight, relief="groove", command=lambda: playClick(stack, None), bg=headerColor)
        empty_stack.place(relx=stack.x[0], rely=stack.y[0])
    else:
        for card in stack:
            renderPlayCard(card, stack_location, stack)

def renderPlayCard(card, location, origin):
    if card.face: # if card is faceUp, then render it as a button
        rendered_card = tk.Button(location, text=card.name, width=cardWidth, height=cardHeight, relief="groove", command=lambda: playClick(origin, card))
    else: # else render it as a Frame (TODO: make back of card nicer)
        rendered_card = tk.Frame(location, borderwidth=2, relief="groove")
        card_label = tk.Label(rendered_card, text='', justify="center", wraplength=40, height=cardHeight, width=cardWidth, bg=cardColor, fg=textColor)
        card_label.pack(side="top", anchor="n")
    rendered_card.place(relx=card.x, rely=card.y)

def playClick(stack, card):
    global selectedCard, selectedStack, chosen, num_cards
    if chosen == False:
        selectedCard = card
        selectedStack = stack
        chosen = True
    elif chosen == True:
        num_cards = len(selectedStack) - selectedStack.cards.index(selectedCard) 
        print(num_cards)
        moveCards(selectedStack, stack, num_cards) 
        chosen = False

# function to render a home stack
def renderHomeStack(stack, stack_location): 
    if len(stack) == 0: # empty stack (no cards)
        empty_stack = tk.Button(stack_location, width=cardWidth, height=cardHeight, relief="groove", command=lambda: homeClick(stack), bg=headerColor)
        empty_stack.place(relx=stack.x[0], rely=stack.y[0])
    else:
        for card in stack:
            renderHomeCard(card, stack_location, stack)
    
def renderHomeCard(card, location, origin):
    if card.face: # if card is faceUp, then render it as a button
        rendered_card = tk.Button(location, text=card.name, width=cardWidth, height=cardHeight, relief="groove", command=lambda: homeClick(origin))
    else: # else render it as a Frame (TODO: make back of card nicer)
        rendered_card = tk.Frame(location, borderwidth=2, relief="groove")
        card_label = tk.Label(rendered_card, text='', justify="center", wraplength=40, height=cardHeight, width=cardWidth, bg=cardColor, fg=textColor)
        card_label.pack()
    rendered_card.place(relx=card.x, rely=card.y)

# function for clicking cards in the home stacks 
def homeClick(stack):
    global selectedCard, selectedStack, chosen
    if chosen == False and len(stack) > 0:
        selectedCard = stack[-1] # top of the selected home stack
        selectedStack = stack
        chosen = True
    elif chosen == True:
        moveCards(selectedStack, stack, 1)

# function for clicking stockpile
def stockClick():
    global stock, waste
    if len(stock) == 0:
        # flip every card in waste back, set the waste pile to the stock pile
        # set the waste pile to an empty stack
        # shuffle the stock pile
        # renderBoard()
        for card in waste:
            card.flip()
        stock += waste
        stock.shuffle()
        waste = Stack()
        renderBoard()
    else:
        # add the card at the top of the stock to the waste
        # remove that card from the stock
        # renderBoard()
        card = stock.pop()
        card.flip()
        waste.append(card)
        updateDisplay()

# render each of the labels in the board
def renderLabels():
    # stock label
    stock_label = tk.Label(board, text="Stockpile", bg=bgColor, fg=textColor)
    stock_label.place(relx=0.09, rely=0.05)
    # waste label
    waste_label = tk.Label(board, text="Waste Pile", bg=bgColor, fg=textColor)
    waste_label.place(relx=0.19, rely=0.05)
    # home label
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
    # set the relative position of the foundation stacks/home stacks, then render them
    foundation_spacing = 0
    for stack in homeStacks:
        stack.x = (0.5 + foundation_spacing, 0)
        stack.y = (0.15, 0.01)
        stack.tidy()
        foundation_spacing = foundation_spacing + 0.1 # <- change this value if needed
        renderHomeStack(stack, board)
    # set the relative position of the tablaeu stacks/play stacks, then render them
    talbeau_spacing = 0
    for stack in playStacks:
        stack.x = (0.2 + talbeau_spacing, 0)
        stack.y = (0.5, 0.025)
        talbeau_spacing = talbeau_spacing + 0.1
        stack.tidy()
        renderPlayStack(stack, board)
    # render the top of stockpile as a button
    stock_top = tk.Button(board, width=cardWidth, height=cardHeight, relief="groove", command=stockClick, bg=cardColor)
    stock_top.place(relx=stock.x[0], rely=stock.y[0])
    # render the waste pile if there are any cards in it
    waste.tidy()
    renderWasteStack(waste, board)
    # render the labels
    renderLabels()


# function to clear all the widgets from the board
def clearBoard():
    for widgets in board.winfo_children():
        widgets.destroy()

# call once at the start of a game, potentially every time a move is made (it's a bit messy, but would work)
def updateDisplay():
    clearBoard()
    renderBoard()

# call once at the start of a game
def initializeNewGame():
    startGame()
    updateDisplay()

# create the tkinter window
window = tk.Tk()
window.geometry("700x400")
window.title("Python Solitaire")
window.configure(bg=headerColor)

# create the game board
board_width = 700
board_height = 360
board = tk.Frame(window, width=board_width, height=board_height, bg=bgColor)

# create the top UI
top_frame = tk.LabelFrame(window, text="Info", height=40, width=600, bg=headerColor, fg=textColor)
timer_label = tk.Label(top_frame, text=f"Time:{endTime}", bg=headerColor, fg=textColor)
timer_label.grid(row=0, column=0, padx=10)
moves_label = tk.Label(top_frame, text=f"Moves:{moves}", bg=headerColor, fg=textColor)
moves_label.grid(row=0, column=1, padx=10)
score_label = tk.Label(top_frame, text=f"Score:{score}", bg=headerColor, fg=textColor)
score_label.grid(row=0, column=2, padx=10)
top_frame.pack()

# function to update the moves and score labels, can be called once every move
def updateScore():
    moves_label.config(text=f"Moves:{moves}")
    score_label.config(text=f"Score:{score}")

# function to update the timer label, is called once every 1000 ms (1 second)
def updateTime():
    timer_label.config(text=f"Time:{gameTime()}")
    window.after(1000, updateTime)

# function to create a "How to Play" window and close it
def howToPlay():
    popup_window = tk.Toplevel()
    popup_window.title("How to Play")
    
    # Create a label to display the message
    label = tk.Label(popup_window, text="How to goes here") # TODO: write How to play
    label.pack(padx=20, pady=20)

    # Add a button to close the pop-up window
    close_button = tk.Button(popup_window, text="Close", command=popup_window.destroy)
    close_button.pack(pady=10)

# function to create an "About" window and close it
def about():
    popup_window = tk.Toplevel()
    popup_window.title("About")
    
    # Create a label to display the message
    label = tk.Label(popup_window, text="About goes here") # TODO: write about
    label.pack(padx=20, pady=20)

    # Add a button to close the pop-up window
    close_button = tk.Button(popup_window, text="Close", command=popup_window.destroy)
    close_button.pack(pady=10)

# delete this and the associated menu button later
def Cheat():
    print(f"Stockpile: (with ruleFunc{stock.rule})")
    print(stock)
    
    print("\nWaste Pile:")
    print(waste)
    
    print("\nFoundation Piles:")
    for i, stack in enumerate(homeStacks):
        print(f"Foundation {i + 1}:")
        print(stack)
    
    print("\nTableau Piles:")
    for i, stack in enumerate(playStacks):
        print(f"Tableau {i + 1}:")
        print(stack)

# Create the menu and functions (TODO: connect each menu option to an appropriate function)
menubar = tk.Menu(window)
filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label="New Game", command=initializeNewGame)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=window.quit)
menubar.add_cascade(label="Game", menu=filemenu)

helpmenu = tk.Menu(menubar, tearoff=0)
helpmenu.add_command(label="How to Play", command=howToPlay)
helpmenu.add_command(label="About...", command=about)
helpmenu.add_command(label="Cheat", command=Cheat)
menubar.add_cascade(label="Help", menu=helpmenu)

window.config(menu=menubar)

# helper function for debugging; should be removed in final product
def on_key_press(event):
    if event.keysym == '1': # check absolute position of pointer on board
        x = event.x - board.winfo_x()
        y = event.y - board.winfo_y()
        print(f"Mouse Coordinates (relative to board): x={x}, y={y}")
    elif event.keysym == '2': # check what the selected card is
        print(f"Selected card: {selectedCard}, parent is {selectedCard.parent}")
    elif event.keysym == '3': # check what the selected stack is
        print(f"Selected stack: {str(selectedStack)}")
    elif event.keysym == '4': # check board dimentions (not window)
        print(f"Board Dimensions: {board.winfo_width()}x{board.winfo_height()}")
    elif event.keysym == '5':
        print(f"Chosen is: {chosen}")
    elif event.keysym =='6':
        testStack = Stack(ruleFunc=homerule)
        print(testStack.rule)
    elif event.keysym == '7':
        global num_cards
        num_cards = 2
    elif event.keysym == 'r': # reload the board
        for stack in allStacks:
            stack.tidy()
        clearBoard()
        renderBoard()
    elif event.keysym == 's': #show game state
        print(f"Game state: {gameState}")
# bind the functions to window
window.bind('<Key>', on_key_press)

# these functions should be called once at the start of the game
updateTime() # doesn't work?
initializeNewGame()

board.pack(side= "left", expand=True, fill="both")
# main loop
window.mainloop()

# Issues:
# can't see the card's label unless it's at the bottom of the deck. 
# seems to be a tkinter limitation with buttons, unfortunately
# adding a King into an empty play stack (index out of bounds)
# finishing the game
# update score, moves, timer, and labels
