import random
import time, tkinter
from tkinter import Tk,Button, DISABLED, messagebox

#creating a Tkinter window
root = Tk()
root.title('Matchmaker')
root.geometry("600x380")

buttons = {}
first = True
prevX = 0
prevY = 0
moves =0
pairs =0

button_symbols = {}
symbols = [u'\u2702', u'\u2702', u'\u2705', u'\u2705', u'\u2708', u'\u2708', u'\u2709', u'\u2709', u'\u270A', u'\u270A', u'\u270B', u'\u270B', u'\u270C', u'\u270C', u'\u270F', u'\u270F', u'\u2712', u'\u2712', u'\u2714', u'\u2714', u'\u2716', u'\u2716', u'\u2728', u'\u2728',u'\u2733', u'\u2733', u'\u2734', u'\u2734', u'\u2744', u'\u2744']

random.shuffle(symbols)


def close_window():
    global root
    root.quit()

def show_symbol(x,y):
    global first, prevX, prevY, moves, pairs

    buttons[x, y]['text']= button_symbols[x,y]
    buttons[x, y].update_idletasks()

    if first:
        prevX = x
        prevY = y
        first = False
        moves = moves + 1
    elif prevX != x or prevY != y:
        if buttons[prevX, prevY]['text'] != buttons[x, y]['text']:
            time.sleep(0.5)
            buttons[prevX, prevY]['text'] = ''
            buttons[x, y]['text'] = ''
        else:
            buttons[prevX, prevY]['command'] = DISABLED
            buttons[x, y]['command'] = DISABLED
            pairs = pairs + 1
            if pairs == len(buttons)/2:
                messagebox.showinfo('Matching', 'Number of moves: ' + str(moves), command=close_window())

        first = True

for x in range(6):
    for y in range(5):
        button = Button(command=lambda x=x, y=y: show_symbol(x,y), width=3, height=1, font=("Helvetica", 32))
        button.grid(column=x, row=y)
        buttons[x, y] = button
        button_symbols[x,y] = symbols.pop()
root.mainloop()