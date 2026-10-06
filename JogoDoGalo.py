import random as rand
from tkinter import *
from tkinter import ttk
import time

player_turn = None
x = rand.randint(0, 1)

root = Tk()
root.geometry("600x600")

style = ttk.Style()
style.configure("Big.TButton", font=("Arial", 120, "bold"))

buttons = {}

board = [
    ["", "", ""],
    ["", "", ""],
    ["", "", ""]
]

def verify_victory():
    global board
    
    for r in range(len(board)):
        if len(set(board[r])) == 1 and board[r][0] != "":
            print(f"Game Finished: {board[r][0]} won!")
            root.destroy()
            return
    
    for c in range(3): 
        if len({row[c] for row in board}) == 1 and board[0][c] != "":
            print(f"Game Finished: {board[0][c]} won!")
            root.destroy()
            return
    
    if len({board[i][i] for i in range(len(board))}) == 1 and board[1][1] != "":
        print(f"Game Finished: {board[1][1]} won!")
        root.destroy()
        return
    
    if len({board[i][2 - i] for i in range(len(board))}) == 1 and board[1][1] != "":
        print(f"Game Finished: {board[1][1]} won!")
        root.destroy()
        return

    return
    
def first_to_play():
    global player_turn
    global x
    
    if player(x) == "X":
        player_turn = True
        print("Player is First")
    else:
        player_turn = False
        print("Opponent is First")
        root.after(1000, lambda: opponent_play(opponent()))

def opponent_play(opponent):
    global player_turn
    global board

    empty_buttons = [pos for pos, btn in buttons.items() if btn.cget("text") == ""]
    if not empty_buttons:
        return

    r, c = rand.choice(empty_buttons)
    buttons[(r, c)].config(text=opponent)
    board[r][c] = f"{opponent}"
    verify_victory()
    
    player_turn = True

def create_button(r, c, player):
    btn = ttk.Button(root, style="Big.TButton", command=lambda: click(r, c, player))
    btn.grid(row=r, column=c, sticky="nsew")
    buttons[(r, c)] = btn

def click(r, c, player):
    global player_turn
    
    if not player_turn:
        return

    if buttons[(r, c)].cget("text") != "":
        return
    
    board[r][c] = f"{player}"
    buttons[(r, c)].config(text=player)
    verify_victory()
    player_turn = False
    root.after(1000, lambda: opponent_play(opponent()))
       
def initiate_game(player):
    for i in range(3):
        root.rowconfigure(i, weight=1)
        root.columnconfigure(i, weight=1)

    for r in range(3):
        for c in range(3):
            create_button(r, c, player)

def player(x):
    if x == True:
        return "X"
    else:
        return "O"

def opponent():
    if player(x) == "X":
        return "O"
    else:
        return "X"
    
initiate_game(player(x))

root.after(5000, first_to_play)
    
root.mainloop()