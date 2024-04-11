import tkinter as tk
from card import *

def renderCard(card, location, cardx, cardy):
    # TODO: fix this
    rendered_card = tk.Frame(location, borderwidth=2, width=card.w, height=card.h, relief="groove")
    card_label = tk.Label(rendered_card, text=str(card.value) + " of " + card.suit, justify="center", wraplength=40, height=3)
    card_label.pack()
    rendered_card.place(x=cardx, y=cardy)


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

stock_label = tk.LabelFrame(left_frame, text="Stock", padx=5, pady=5, width=55, height=80, borderwidth=2, relief="sunken")
stock_label.pack()

waste_label = tk.LabelFrame(left_frame, text="Waste", padx=5, pady=5, width=55, height=80, borderwidth=2, relief="sunken")
waste_label.pack()

left_frame.pack( side = "left")


# Create the right-side frame (contains the foundation stacks)
right_frame = tk.Frame(window, width=60, height=260, padx=5)

foundation_pile1 = tk.LabelFrame(right_frame, text="Pile 1", padx=5, pady=5, width=55, height=80, borderwidth=2, relief="sunken")
foundation_pile1.grid(row=0, column=0, pady=5)

foundation_pile2 = tk.LabelFrame(right_frame, text="Pile 2", padx=5, pady=5, width=55, height=80, borderwidth=2, relief="sunken")
foundation_pile2.grid(row=1, column=0, pady=5)

foundation_pile3 = tk.LabelFrame(right_frame, text="Pile 3", padx=5, pady=5, width=55, height=80, borderwidth=2, relief="sunken")
foundation_pile3.grid(row=2, column=0, pady=5)

foundation_pile4 = tk.LabelFrame(right_frame, text="Pile 4", padx=5, pady=10, width=55, height=80, borderwidth=2, relief="sunken")
foundation_pile4.grid(row=3, column=0, pady=5)

right_frame.pack(side = "right")


# Create the center/bottom-side frame (tablaeu)
tablaeu = tk.Frame(window, height=250, width=500)

i = 0
for x in range(7):
    i=i+1
    x = tk.LabelFrame(tablaeu, text=str(i), padx=5, width=55, height=250)
    x.grid(row=0, column=i, padx=10)

tablaeu.pack( side = "top")

# test methods/stuff
test_card = Card(value=4, suit='s', width=30, height=40)
renderCard(test_card, x, 0, 0)

temp_button = tk.Button(window, text="Undo", padx=10, pady=10)
temp_button.pack( side = "bottom")

# main loop
window.mainloop()

# TODO: 
#   * add padding to each of the frames where necessary
#   * create method to render a card and display it, possibly as a button?
#   * make the timer work
#   * use ipadx, ipady to manage each widget's borders in grid() instead of applying to each widget manually?
#   * possibly use grid() instead of pack(), since it has more options?
#   * use for loops to create each of the stacks
#   * use variables for each of the pile sizes (length and width) instead of hardcoding, also lets you change them elsewhere
